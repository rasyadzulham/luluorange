# luluorange🍊
Link to project: https://rasyad-zulham-luluorange.pbp.cs.ui.ac.id/

## Tugas 2
### Step by step implementasi checklist✅

#### Inisiasi
1. Membuat direktori luluorange, membuat virtual environment pada direktori tersebut dengan
   ~~~
   python3 -m venv env
   ~~~
   dan mengaktifkannya dengan
   ~~~
   source env/bin/activate
   ~~~
2. Membuat requirements.txt dan mengisinya dengan
   ~~~
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   python-dotenv
   ~~~
   kemudian menginstall dependencies yang ada di file tersebut dengan
   ~~~
   pip install -r requirements.txt
   ~~~
3. Membuat proyek django dengan perintah
   ~~~
   django-admin startproject luluorange .
   ~~~
4. Membuat file .env dan .env.prod untuk konfigurasi environment variables yang berisi
   ~~~
   # file .env
   PRODUCTION=False
   ~~~
   ~~~
   # file .env.prod
   DB_NAME=<rasyad.zulham>
   DB_HOST=<...>
   DB_PORT=<...>
   DB_USER=<rasyad.zulham>
   DB_PASSWORD=<...>
   SCHEMA=tugas_individu
   PRODUCTION=True
   ~~~
5. Membuat aplikasi main dalam proyek luluorange dengan
   ~~~
   python manage.py startapp main
   ~~~
6. Memodifikasi settings.py seperti pada tutorial 0
   ```python
   # Untuk mengguankan virtual environment
   from dotenv import load_dotenv
   # Load environment variables from .env file
   load_dotenv()
   ```
   ```python
   # Menambahkan allowed_hosts
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ```
   ```python
   # Konfigurasi production
   PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'
   ```
   ```python
   # Database configuration
    if PRODUCTION:
        # Production: gunakan PostgreSQL dengan kredensial dari environment variables
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('DB_NAME'),
                'USER': os.getenv('DB_USER'),
                'PASSWORD': os.getenv('DB_PASSWORD'),
                'HOST': os.getenv('DB_HOST'),
                'PORT': os.getenv('DB_PORT'),
                'OPTIONS': {
                    'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
                }
            }
        }
    else:
        # Development: gunakan SQLite
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
   ```
   ```python
   INSTALLED_APPS = [
    ...
    'main',
   ]
   ```


#### Membuat models, views, dan template

7. Memodifikasi berkas models.py pada aplikasi main, membuat model dengan nama Product, dan memasukkan atribut-atribut wajib yang tertera pada dokumen soal
   ```python
   from django.db import models

   class Product(models.Model):
       CATEGORY_CHOICES = [
           ('atasan', 'Atasan'),
           ('bawahan', 'Bawahan'),
           ('sepatu', 'Sepatu'),
           ('aksesoris', 'Aksesoris'),
       ]

    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    ```
8. Lakukan migrasi model dengan
   ~~~
   python manage.py migrate
   ~~~
9. Menambahkan fungsi show_main pada file views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
    ```python
    def show_main(request):
    context = {
        'npm' : '2406348540',
        'name': 'Rasyad Zulham Rabani',
        'app': 'Luluorange'
    }

    return render(request, "main.html", context)
    ```
10. Membuat direktori templates pada aplikasi main lalu membuat file main.html yang berisi nama aplikasi, nama, dan kelas menggunakan sintaks Django {{ app }}, {{ name }} dan {{ class }}, agar bisa menampilkan nilai dari variabel yang telah didefinisikan dalam context pada fungsi show_main
    ```html
    <h1>{{ app }}</h1>

    <h4>Name: </h4>
    <p>{{ name }}</p> 
    <h4>NPM: </h4>
    <p>{{ npm }}</p>
    <h4>Class: </h4>
    <p>{{ class }}</p>
    ```

#### Melakukan routing URL

11. Untuk mengonfigurasi routing URL aplikasi main, buat urls.py pada aplikasi main dan mengisinya dengan URL pattern yang kita kehendaki
    ```python
    from django.urls import path
    from main.views import show_main
      
    app_name = 'main'
      
    urlpatterns = [
       path('', show_main, name='show_main'),
    ]
    ```
12. Untuk mengonfigurasi routing URL proyek, buka urls.py pada direktori proyek dan mengisinya dengan URL pattern yang kita kehendaki (Menggunakan include('main.urls') untuk mengimpor pola rute URL dari aplikasi main ke dalam berkas urls.py level proyek)
    ```python
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    ]
    ```
13. Menjalankan server untuk melihat apakah aplikasi web sudah sesuai dengan harapan
    ~~~
    python3 manage.py runserver
    ~~~
    
#### Deployment ke PWS

14. Buat file .gitignore untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git.
15. Buka PWS dan create new project, lalu copy paste isi file .env.prod ke tab environs pada project yang baru dibuat
16. Update allowed-host pada file settings.py (menambahkan URL Deployment PWS "rasyad-zulham-luluorange.pbp.cs.ui.ac.id")
17. Jalankan command di bawah ini lalu masukkan username serta password
    ~~~
    git remote add pws https://pbp.cs.ui.ac.id/rasyad.zulham/luluorange
    git branch -M master
    git push pws master
    ~~~
18. Apabila status proyek 'running', maka bisa klik view project
    
### Request-Response Cycle💫

<img width="1130" height="635" alt="Screen Shot 2025-09-08 at 21 02 44" src="https://github.com/user-attachments/assets/cec128c2-93e2-4a98-8775-afdf70b52a8b" />

## Peran settings.py dalam proyek Django🐍
File settings.py sering disebut juga dengan jantung dari proyek Django. Settings.py berperan sebagai pusat penghubung untuk setting Django yang berisi semua konfigurasi dari instalasi Django serta mengontrol banyak aspek seperti konfigurasi database, installed application, konfigurasi URL, static file directories, dan masih banyak lagi. 

Source: https://dev.to/rupesh_mishra/understanding-djangos-settingspy-file-a-comprehensive-guide-for-beginners-35e2#:~:text=The%20settings.py%20file%20is,file%20directories%2C%20and%20much%20more.

### Cara kerja migrasi database di Django
Migrasi database di Django adalah mekanisme untuk menjaga skema database (tabel, kolom, relasi, constraint) tetap sinkron dengan model Python yang telah didefinisikan pada file models.py. Django tidak langsung mengubah database ketika mengubah models.py. Oleh karena itu, jalankan command
~~~
python3 manage.py makemigrations
~~~
Dengan ini, Django akan membaca perubahan pada model, lalu membuat file migrasi di folder migrations/.
File migrasi berisi instruksi Python untuk membentuk atau mengubah tabel di database.
Untuk menerapkan perubahan ke database, jalankan command
~~~
python3 manage.py migrate
~~~
Django akan membaca semua file migrasi yang belum pernah dijalankan, lalu mengeksekusi SQL akan dijalankan hingga pada akhirnya database sekarang sinkron dengan model.

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Untuk menguasai sebuah framework, kita harus memiliki landasan kuat dalam bahasa pemrograman yang digunakan oleh framework tersebut. Django adalah framework berbasis Python, Python merupakan bahasa pemrograman pengantar pada mata kuliah DDP-1, sehingga saya sudah terbiasa dengan sintaksnya yang akan membuat proses pembelajaran akan lebih mudah. Dari beberapa sumber yang saya baca, Django adalah framework web tingkat tinggi yang menyediakan banyak fitur bawaan, sehingga memungkinkan kita untuk membangun aplikasi dengan cepat. Django juga memiliki dokumentasi yang sangat baik dan kuat dengan komunitas yang aktif, sehingga mudah untuk belajar dan mendapatkan bantuan jika diperlukan.

### Feedback untuk asisten dosen di tutorial 1
Overall tutorialnya sangat jelas dan detail, saya bisa mengikutinya dengan baik. Jika ada kesulitan, asisten dosen pun dengan sigap membantu menyelesaikan problem. 

## Tugas 3
### Step by step implementasi checklist✅
#### Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
```python
# views.py
def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
     product_list = Product.objects.all()
     json_data = serializers.serialize("json", product_list)
     return HttpResponse(json_data, content_type="application/json")

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
```
#### Membuat routing URL untuk masing-masing views yang telah ditambahkan
```python
# urls.py di aplikasi
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
   ...
]
```

#### Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
1.  Buat direktori templates pada root dan buat file base.html didalamnya
```python
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
</head>

<body>
    {% block content %} {% endblock content %}
</body>
</html>
```
2. Konfigurasi base directory template pada settings.py
```python
TEMPLATES = [
    {
      ...
      'DIRS': [BASE_DIR / 'templates'],
      ...
    }
```
3. Modifikasi file main.html di templates aplikasi agar ada tombol add, menampilkan objek, dan show details
```python
 {% extends 'base.html' %}
 {% block content %}
 <h1>Luluorange</h1>

<h5>NPM: </h5>
<p>{{ npm }}</p>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>

<a href="{% url 'main:add_product' %}">
  <button>+ Add Product</button>
</a>

<hr>

{% if not product_list %}
<p>Belum ada product yang dijual.</p>
{% else %}

{% for product in product_list %}
<div>
    {% if product.thumbnail %}
    <img src="{{ product.thumbnail }}" alt="thumbnail" width="150">
    <br />
    {% endif %}
    
  <h2><a href="{% url 'main:show_product' product.id %}">{{ product.name }}</a></h2>
  <h3><b>Rp. {{ product.price }}</b></h3>

  <p><b>{{ product.get_category_display }}
    </b>{% if product.is_featured %} | <b>Featured</b>{% endif %}
    {% if product.is_product_recommended %} | <b>Loved by Everyone!</b>{% endif %} | <b>Rating: {{ product.rating }}/5</b></p>

    <p>{{ product.description|truncatewords:25 }}...</p>

  <p><a href="{% url 'main:show_product' product.id %}"><button>See Details</button></a></p>
</div>

<hr>
{% endfor %}

{% endif %}
{% endblock content %}
```
#### Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
1. Buat forms.py di direktori aplikasi
```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "price", "description", "is_featured", "thumbnail", "rating"]
```
2. Buat file add_product.html di direktori templates aplikasi
```python
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
3. Tambahkan fungsi add_product pada views.py
```python
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)
```
4. Routing URL pada urls.py aplikasi
```python
urlpatterns = [
    ...
    path('add-product/', add_product, name='add_product'),
    ...
]
```
5. Pada settings.py tambahkan CSRF_TRUE_ORIGIN setelah ALLOWED_HOSTS
```python
...
CSRF_TRUSTED_ORIGINS = [
    "https://rasyad-zulham-luluorange.pbp.cs.ui.ac.id/"
]
...
```
#### Membuat halaman yang menampilkan detail dari setiap data objek model.
1. Buat file product_detail.html di direktori templates aplikasi
```python
{% extends 'base.html' %}
{% block content %}
<p><a href="{% url 'main:show_main' %}"><button>← Back to Product List</button></a></p>

{% if product.thumbnail %}
<img src="{{ product.thumbnail }}" alt="Product thumbnail" width="300">
<br /><br />
{% endif %}

<h1>{{ product.name }}</h1>
<h2><b>Rp. {{ product.price }}</b></h2>

<p><b>{{ product.get_category_display }}
    </b>{% if product.is_featured %} | <b>Featured</b>{% endif %}
    {% if product.is_product_recommended %} | <b>Loved by Everyone!</b>{% endif %}</p>

<p>{{ product.description }}</p>

{% endblock content %}
```
2. Tambahkan fungsi show_product pada views.py
```python
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)
```
3. Routing URL pada urls.py aplikasi
```python
urlpatterns = [
    ...
    path('product/<str:id>/', show_product, name='show_product'),
    ...
]
```


