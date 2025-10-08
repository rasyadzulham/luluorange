from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
import datetime
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    elif filter_type == "atasan":
        product_list = Product.objects.filter(category='atasan')
    elif filter_type == "bawahan":
        product_list = Product.objects.filter(category='bawahan')
    elif filter_type == "sepatu":
        product_list = Product.objects.filter(category='sepatu')
    elif filter_type == "aksesoris":
        product_list = Product.objects.filter(category='aksesoris')
    elif filter_type == "bola":
        product_list = Product.objects.filter(category='bola')
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406348540',
        'name': request.user.username,
        'app': 'Luluorange',
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

from django.http import JsonResponse
from .models import Product 
# Pastikan Anda sudah mengimpor model Product Anda di bagian atas views.py

def show_json(request):
     product_list = Product.objects.all()
     
     data = []
     for product in product_list:
        
        # Penanganan User (mengambil ID dan username, bukan objek User)
        if product.user:
            user_id = product.user.pk
            owner_name = product.user.username
        else:
            user_id = None
            owner_name = 'Anonymous'
        
        # Penanganan Thumbnail (mengambil URL, bukan objek FileField)
        image_url = product.thumbnail if product.thumbnail else ''
        
        data.append({
            'id': str(product.id), # ID harus string
            'user_id': user_id,
            'owner_name': owner_name, # Digunakan di JS untuk menampilkan nama pemilik
            
            'name': product.name,
            'price': product.price,
            'category': product.category,
            # Pastikan field ini ada dan ditangani jika mungkin None
            'rating': product.rating if product.rating is not None else 0, 
            'description': product.description,
            'is_featured': product.is_featured,
            
            'image_url': image_url, # Key 'image_url' digunakan di JS frontend
        })
        
     # safe=False karena kita mengembalikan list, bukan dictionary utama
     return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        json_data = serializers.serialize("json", product_item)
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()

    return JsonResponse({'success': True, 'message': 'Product deleted successfully.'})

@csrf_exempt 
def update_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            product_data = model_to_dict(product)
            product_data["category_display"] = product.get_category_display()
            product_data["is_product_recommended"] = float(product.rating) >= 4.0
            return JsonResponse({
                'success': True,
                'message': 'Product updated successfully!',
                'product': model_to_dict(product)
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        # untuk prefill modal
        return JsonResponse(model_to_dict(product))
    
@login_required(login_url='/login')
@require_POST
def add_product_ajax(request):
    # Cek apakah metode POST sudah diatur oleh require_POST
    form = ProductForm(request.POST)
    if form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        
        # RESPONSE SUKSES YANG MINIMALIS
        return JsonResponse({
            'success': True,
            'product_id': str(product_entry.id),
        }, status=200) # Status 200 OK untuk sukses
    else:
        # Pastikan response error menggunakan status 400
        # dan mengirim error details
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)