# luluorange🍊
Link to project: https://rasyad-zulham-luluorange.pbp.cs.ui.ac.id/

Comprehensive explanation for every assignment👇🏻

<details>
<summary>Tugas 2</summary>

## Step by step implementasi checklist✅

### Inisiasi
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


### Membuat models, views, dan template

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

### Melakukan routing URL

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
    
### Deployment ke PWS

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
    
## Request-Response Cycle💫

<img width="1130" height="635" alt="Screen Shot 2025-09-08 at 21 02 44" src="https://github.com/user-attachments/assets/cec128c2-93e2-4a98-8775-afdf70b52a8b" />

## Peran settings.py dalam proyek Django🐍
File settings.py sering disebut juga dengan jantung dari proyek Django. Settings.py berperan sebagai pusat penghubung untuk setting Django yang berisi semua konfigurasi dari instalasi Django serta mengontrol banyak aspek seperti konfigurasi database, installed application, konfigurasi URL, static file directories, dan masih banyak lagi. 

Source: https://dev.to/rupesh_mishra/understanding-djangos-settingspy-file-a-comprehensive-guide-for-beginners-35e2#:~:text=The%20settings.py%20file%20is,file%20directories%2C%20and%20much%20more.

## Cara kerja migrasi database di Django
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

## Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Untuk menguasai sebuah framework, kita harus memiliki landasan kuat dalam bahasa pemrograman yang digunakan oleh framework tersebut. Django adalah framework berbasis Python, Python merupakan bahasa pemrograman pengantar pada mata kuliah DDP-1, sehingga saya sudah terbiasa dengan sintaksnya yang akan membuat proses pembelajaran akan lebih mudah. Dari beberapa sumber yang saya baca, Django adalah framework web tingkat tinggi yang menyediakan banyak fitur bawaan, sehingga memungkinkan kita untuk membangun aplikasi dengan cepat. Django juga memiliki dokumentasi yang sangat baik dan kuat dengan komunitas yang aktif, sehingga mudah untuk belajar dan mendapatkan bantuan jika diperlukan.

## Feedback untuk asisten dosen di tutorial 1
Overall tutorialnya sangat jelas dan detail, saya bisa mengikutinya dengan baik. Jika ada kesulitan, asisten dosen pun dengan sigap membantu menyelesaikan problem. 
</details>

<details>
<summary>Tugas 3</summary>

## Step by step implementasi checklist✅
### Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
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
### Membuat routing URL untuk masing-masing views yang telah ditambahkan
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

### Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
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
### Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
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
### Membuat halaman yang menampilkan detail dari setiap data objek model.
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
## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?📦
Dalam pengimplementasian sebuah platform, data delivery sangat penting karena menjadi tulang punggung komunikasi antar komponen, mulai dari front-end, back-end, database, hingga integrasi dengan layanan pihak ketiga. Mekanisme ini memastikan data dapat ditransfer dengan konsisten, efisien, dan andal, sehingga setiap perubahan pada sistem segera tersampaikan ke seluruh bagian platform tanpa menimbulkan inkonsistensi. Selain itu, data delivery mendukung skalabilitas dengan menjaga performa ketika jumlah pengguna meningkat, serta memberikan reliabilitas melalui mekanisme retry dan error handling agar data tidak hilang meskipun terjadi gangguan. Dengan demikian, data delivery menjadikan platform berfungsi sebagai sebuah sistem yang utuh, bukan sekadar kumpulan modul terpisah.

## XML vs JSON
Menurut saya, JSON lebih unggul karena lebih simpel, fleksibel, dan cepat dibandingkan dengan XML. JSON lebih populer dibandingkan XML karena sifatnya yang lebih ringan, sederhana, dan mudah dibaca baik oleh manusia maupun mesin. JSON tidak menggunakan banyak tag seperti XML sehingga ukuran datanya lebih kecil dan proses parsing lebih cepat, membuatnya sangat efisien untuk kebutuhan komunikasi data di web modern, aplikasi mobile, serta layanan API seperti REST dan GraphQL. Selain itu, hampir semua bahasa pemrograman menyediakan dukungan bawaan atau pustaka JSON yang mudah digunakan, sehingga developer cenderung memilihnya sebagai standar. Sebaliknya, XML masih banyak digunakan di sistem enterprise atau aplikasi legacy yang membutuhkan validasi ketat, namespace, serta struktur dokumen kompleks, misalnya dalam SOAP atau konfigurasi perangkat. Namun, dengan tren teknologi yang semakin mengutamakan kecepatan, kesederhanaan, dan efisiensi, JSON kini menjadi pilihan utama untuk pertukaran data.

## Fungsi dari method is_valid()
Method ini akan mereturn True jika form sudah diisi (bound) dan tidak memiliki error. Jika salah satu tidak terpenuhi, method akan mereturn False. Kita membutuhkan method ini untuk memastikan data pada form valid sebelum dimasukkan ke database. Dengan ini, kualitas data tetap terjaga dan sistem bisa berjalan stabil.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF terjadi ketika penyerang mencoba membuat pengguna yang sudah login di suatu website tanpa sadar mengirimkan request berbahaya (misalnya transfer uang, ubah password) melalui link atau script dari situs lain. 

Contoh kasus jika tanpa csrf_token.
source: https://stackoverflow.com/questions/5207160/what-is-a-csrf-token-what-is-its-importance-and-how-does-it-work#comment68126014_33829607
1. Login di internet banking dan ingin transfer uang
```
https://www.klikbca.com/transfer?to=<SomeAccountnumber>&amount=<SomeAmount>
```
2. Membuka suatu web yang ternyata malicious
3. Jika pemilik dari malicious website itu mengetahui form dari request dan menebak kita sekarang lagi login klikbca, mereka bisa memasukkan request di page mereka seperti:
```
(https://www.klikbca.com/transfer?to=123456&amount=5000000
```
dimana 123456 adalah rekening mereka, and 5000000 amount transfer yang memang mau kita kirim.

4. Kita buka lagi web malicious itu, jadi browser kita memproses request jahat itu.
5. Karena bank tidak bisa mengetahui asal dari request tersebut. Jadi browser bakal kirim requestnya bersamaan dengan cookie www.klikbca.com dan requestnya bakal terlihat seperti beneran. Akhirnya, banknya acc dan uangnya pun kesedot.

Disinilah csrf_token digunakan, token ini merupakan angka random besar yang tidak dapat ditebak. Token ini akan diinclude ke web page ketika ditampilkan ke user (selalu berbeda tiap page dan tiap usernya). Pada saat request dikirim, token ini akan diverifikasi kembali oleh server sehingga hanya request dari halaman sah yang diterima.

## Screenshot dari hasil akses URL pada Postman📨
1. xml/
<img width="1440" height="900" alt="Screen Shot 2025-09-15 at 20 38 49" src="https://github.com/user-attachments/assets/77ef71a7-c0d6-4674-bd64-3d32d87c10ca" />
2. json/
<img width="1440" height="900" alt="Screen Shot 2025-09-15 at 20 39 00" src="https://github.com/user-attachments/assets/1cf2656c-409c-4456-87ae-ace585323f31" />
3. xml/product_id
<img width="1440" height="900" alt="Screen Shot 2025-09-15 at 20 39 19" src="https://github.com/user-attachments/assets/9acf56b2-71d2-4f7e-b0c1-12a5e7f889e1" />
4. json/product_id
<img width="1440" height="900" alt="Screen Shot 2025-09-15 at 20 39 11" src="https://github.com/user-attachments/assets/17a2249e-dab3-4b18-a1e0-e366e04fe65a" />

## Feedback untuk asisten dosen di tutorial 2
Pada tutorial 2 dan tugas 3 ini, saya mengalami error di database. Asdos langsung menjawab pertanyaan di tutorial. FAQ di discord juga membantu menyelesaikan sebagian besar permasalahan tersebut.
</details>


<details>
<summary>Tugas 4</summary>
   
## Step by step implementasi checklist✅
### Mengimplementasikan fungsi login
1. Buka views.py tambahkan import pada bagian atas dan fungsi login_user.
```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
...
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
2. Buat login.html pada templates aplikasi
``` html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
3. Buka urls.py tambahkan import login_user dari views.py dan masukkan path untuk login
```python
from main.views import login_user
...
urlpatterns = [
   ...
   path('login/', login_user, name='login'),
]
```

### Mengimplementasikan fungsi logout
1. Buka views.py tambahkan import logout dari django.contrib.auth pada bagian atas dan fungsi logout_user.
```python
from django.contrib.auth import logout
...
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
2. Buka berkas main.html dan tambahkan button untuk logout
``` html
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
3. Buka urls.py tambahkan import logout_user dari views.py dan masukkan path untuk logout
```python
from main.views import logout_user
...
urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
]
```

### Mengimplementasikan fungsi register
1. Buka views.py tambahkan beberapa import untuk form pada bagian atas dan fungsi register.
```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
...
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
```
2. Buat berkas register.html
``` html
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div>
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
3. Buka urls.py tambahkan import register dari views.py dan masukkan path untuk register
```python
from main.views import register
...
urlpatterns = [
     ...
     path('register/', register, name='register'),
 ]
```

### Merestriksi pengguna agar hanya bisa mengakses halaman jika sudah login
1. Tambahkan import decorator rogin_required pada bagian atas views.py
``` python
from django.contrib.auth.decorators import login_required
```
2. Tambahkan potongan kode diatas funsgi show_main dan show product
``` python
@login_required(login_url='/login')
def show_main(request):
...

@login_required(login_url='/login')
def show_product(request, id):
...
```
### Menghubungkan model Product dengan User
1. Buka models.py dan tambahkan import dibagian atas
``` python
...
from django.contrib.auth.models import User
...
```
2. Pada class Product tambahkan field user untuk menghubungkan satu product dengan satu user
```python
user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
```
3. Lakukan migrate karena kita telah melakukan modifikasi pada model
``` bash
python3 manage.py makemigrations
python3 manage.py migrate
```
4. Buka views.py dan ubah fungsi add_product agar bisa menyimpan product sesuai dengan user yang sedang login
``` python
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
```
4. Buka views.py dan ubah fungsi show_main agar bisa memfilter product mana saja yang ditambah oleh user yang sedang login
``` python
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406348540',
        'name': 'Rasyad Zulham Rabani',
        'app': 'Luluorange',
        'class': 'PBP D',
        'product_list': product_list,
    }
```
5. Tambahkan tombol filter all dan my pada main.html
``` html
<a href="?filter=all">
    <button type="button">All Products</button>
</a>
<a href="?filter=my">
    <button type="button">My Products</button>
</a>
```
6. Tampilkan nama author pada akhir product_detail.html, pada kasus ini saya misalkan desainer
``` html
{% if product.user %}
    <p>Designer: {{ product.user.username }}</p>
{% else %}
    <p>Designer: Best designer in the world</p>
{% endif %}
```

### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
1. Buka views.py pada aplikasi main dan Tambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas.
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
2. Ubah bagian kode di fungsi login_user untuk menyimpan cookie baru bernama last_login yang berisi timestamp terakhir kali pengguna melakukan login.
``` python
...
if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
...
```
3. Pada fungsi show_main, ubah context agar dapat menampilkan username yang sedang login dan mengambil waktu terakhir login
```python
context = {
        'npm' : '2406348540',
        'name': request.user.username,
        'app': 'Luluorange',
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
```
4. Ubah fungsi logout agar dapat menghapus cookie last_login
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
4. Tambahkan last_login pada main.html agar dapat ditampilkan ke pengguna
``` python
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

### Membuat dua akun dan tiga dummy data untuk setiap akun di lokal
1. Melakukan register dua akun
2. Melakukan add product ke masing-masing akun sebanyak tiga kali

   
## Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm adalah form bawaan Django yang terdapat di modul django.contrib.auth.forms. Form ini digunakan untuk autentikasi login user (mengecek apakah username dan password valid). Secara default, form ini akan meminta username dan password, melakukan validasi apakah kombinasi keduanya cocok dengan akun yang ada di database, dan menyediakan integrasi langsung dengan sistem authenticate() dan login() dari Django.

### Kelebihan:
1. Tidak perlu implementasi ulang form login, tinggal pakai.
2. Menangani validasi username/password secara langsung dengan authenticate().
3. Bisa langsung dipakai bersama view bawaan Django (LoginView).
4. Sudah mengikuti praktik keamanan standar Django (hashing password, CSRF protection).
5. Bisa ditambah field atau style lewat inheritance.

### Kekurangan:
1. Hanya mendukung username dan password, jika ingin login dengan email atau yang lainnya, perlu di-override.
2. Jika menginginkan fitur tambahan seperti login dengan OTP, social login, atau captcha harus ditambahkan manual.
3. Hanya menyediakan struktur form dasar, tidak ada tampilan cantik; developer harus menyesuaikan template.
4. Tergantung pada model user default, jika pakai custom user model dengan login method berbeda, perlu modifikasi tambahan.

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses memverifikasi identitas seorang user, misalnya seperti username dan password yang diinput benar dan sesuai. Setelah itu, baru dilakukan otorisasi, yaitu proses memberikan akses kepada user yang telah ter-autentikasi. Akses yang diberikan disesuaikan dengan role dari setiap akun. Contohnya admin dan user, pastinya memilki hak akses yang berbeda.

### Implementasi
Django menyediakan sistem autentikasi bawaan lewat django.contrib.auth. Komponen utamanya:
1. User model (django.contrib.auth.models.User) → menyimpan data user.
2. Authentication backends → mekanisme memvalidasi user (default: username + password, tapi bisa ditambah custom backend, misalnya email login).
3. Form dan view → seperti AuthenticationForm, LoginView, dan fungsi authenticate() + login().

Setelah user terautentikasi, Django cek hak aksesnya lewat sistem permissions dan groups. Tiga mekanisme utamanya:

1. is_authenticated → cek apakah user sudah login.
2. is_staff, is_superuser → flag khusus untuk admin/staf.
3. Permissions → bisa di-assign ke user/group.

## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

----- Cookie -----

Kelebihan
- Ringan, tidak memakan resource besar karena disimpan di client
- Dapat diakses oleh semua window di browser
- Bisa digunakan lintas request yang emudahkan "remember me" login atau preferensi user
- Lebih cepat karena data disimpan di client
- Data tetap ada walaupun browser ditutup (kecuali jika kadaluarsa)

Kekurangan
- Cookie hanya dapat menyimpan maksimal 4 KB data
- Kurang aman karena terexposed ke client

---- Session ----

Kelebihan
- Sessions menyimpan data pengguna di server, membuatnya lebih aman dan ideal untuk menyimpan informasi sementara atau informasi yang sensitif
- Bisa menyimpan data dalam jumlah yang besar

Kekurangan
- Sedikit lebih lambat karena setiap request membutuhkan server processing
- Data hilang ketika session kadaluarsa atau server restart (kecuali disimpan di database)

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Terdapat beberapa risiko potensial yang harus diwaspadai dalam penggunaan cookies, diantaranya cross site scripting (XSS) yang memungkinkan pengguna untuk menginjeksi client side scripts ke browser pengguna lain. Menggunakan template Django sudah melindungi dari sebagian besar serangan XSS. Namun, penting untuk memahami sejauh mana perlindungan ini bekerja dan apa saja keterbatasannya.

Cross site request forgery juga bisa menjadi risiko dimana malicious user dapat melakukan aksi menggunakan kredensial dari pengguna lain tanpa izin atau sepengetahuan pengguna tersebut. Django memiliki built in protection untuk menangani CSRF, cara kerjanya adalah dengan memeberikan sebuah CSRF token pada setiap form yang diisi. Django akan memastikan form yang di POST memiliki CSRF token yang sama dengan yang miliki oleh user saat membuka form. Ini memastikan attacker nggak bisa nge-replay form POST ke website dan bikin user lain yang udah login tanpa sadar submit form itu lagi. Attacker harus tahu CSRF token yang sifatnya user-specific (disimpan di cookie).

</details>

<details>
<summary>Tugas 5</summary>

## Step by step implementasi checklist✅
### Mengimplementasikan fungsi untuk menghapus dan mengedit produk🗑
1. Buka views.py di direktori aplikasi dan tambahkan fungsi delete_product dan edit_product
``` python
def edit_product(request, id):
    news = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=news)
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
```
2. Buat edit_product.html pada direktori templates aplikasi
``` html
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit News</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
3. Buka urls.py di direktori aplikasi tambahkan
``` python
# Di paling atas
from main.views delete_product, edit_product

# dalam urlpatterns
urlpatterns = [
    ...
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
]
```
4. Tambahkan tombol edit dan delete product di samping tombol see details pada main.html
``` html
<p>
    <a href="{% url 'main:show_product' product.id %}"><button>See Details</button></a>
    {% if user.is_authenticated and product.user == user %}
    <a href="{% url 'main:edit_product' product.pk %}">
        <button>
            Edit
        </button>
    </a>
    </a>
     <a href="{% url 'main:delete_product' product.pk %}">
      <button>
          Delete
      </button>
    </a>
    {% endif %}
  </p>
```
### Menambahkan tailwind CSS ke aplikasi dan konfigurasi static files⚡️
1. Untuk menyambungkan django dengan tailwind maka kita dapat memanfaatkan Content Delivery Network (CDN) dyang ditambahkan pada base.html
``` html
<head>
{% block meta %}
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
{% endblock meta %}
<script src="https://cdn.tailwindcss.com">
</script>
</head>
```
2. Tambahkan middlewear WhiteNoise pada settings.py
``` python
...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
    ...
]
...
```
3. Tambahkan konfigurasi static pada settings.py
``` python
...
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' # merujuk ke /static root project pada mode development
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
...
```
4. Buat direktori static pada direktori root, buat direktori css, dan buat file global.css
``` css
/* Di sini bisa mendefinisikan kelas styling sendiri */
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #16a34a;
    box-shadow: 0 0 0 3px #16a34a;
}

.form-style input[type="checkbox"] {
    width: 1.25rem;
    height: 1.25rem;
    padding: 0;
    border: 2px solid #d1d5db;
    border-radius: 0.375rem;
    background-color: white;
    cursor: pointer;
    position: relative;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
}

.form-style input[type="checkbox"]:checked {
    background-color: #16a34a;
    border-color: #16a34a;
}

.form-style input[type="checkbox"]:checked::after {
    content: '✓';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-weight: bold;
    font-size: 0.875rem;
}

.form-style input[type="checkbox"]:focus {
    outline: none;
    border-color: #16a34a;
    box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.1);
}
```
5. Ubah base.html pada templates root agar terhubung dengan global.css dan script Tailwind
``` html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
### Styling page login, register, add product, edit product, dan detail product👔
1. Modifikasi login.html
2. Modifikasi register.html
3. Modifikasi edit_product.html
4. Modifikasi detail_product.html

### Styling main page dengan navbar
1. Pada direktori static, buat direktori image dan tambahkan gambar yang akan ditampilkan saat belum ada produk yang terdaftar
2. Buat card_product.html pada direktori templates aplikasi dengan tombol edit dan hapus produk
``` html
...
<!-- Action Buttons -->
    {% if user.is_authenticated and product.user == user %}
      <div class="flex items-center justify-between pt-4 border-t border-gray-100">
        <a href="{% url 'main:show_product' product.id %}" class="text-amber-500 hover:text-amber-600 font-medium text-sm transition-colors">
          See Details →
        </a>
        <div class="flex space-x-2">
          <a href="{% url 'main:edit_product' product.id %}" class="text-gray-600 hover:text-gray-700 text-sm transition-colors">
            Edit
          </a>
          <a href="{% url 'main:delete_product' product.id %}" class="text-red-600 hover:text-red-700 text-sm transition-colors">
            Delete
          </a>
        </div>
      </div>
    {% else %}
      <div class="pt-4 border-t border-gray-100">
        <a href="{% url 'main:show_product' product.id %}" class="text-amber-500 hover:text-amber-600 font-medium text-sm transition-colors">
          See Details →
        </a>
      </div>
    {% endif %}
...
```
3. Buat file navbar.html pada direktori templates root untuk membuat navbar yang responsive terhadap perbedaan ukuran device
4. Modifikasi main.html dengan include navbar.html dan card_product.html
``` html
...
{% include 'navbar.html' %}
...
<!-- Menampilkan gambar dan pesan jika belum ada produk yang terdaftar -->
    {% if not product_list %}
      <div class="bg-white rounded-lg border border-gray-200 p-12 text-center">
        <div class="w-32 h-32 mx-auto mb-4">
          <img src="{% static 'image/no-product.png' %}" alt="No products available" class="w-full h-full object-contain">
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No product found</h3>
        <p class="text-gray-500 mb-6">Be the first to share football news with the community.</p>
        <a href="{% url 'main:add_product' %}" class="inline-flex items-center px-4 py-2 bg-amber-500 text-white rounded-md hover:bg-amber-600 transition-colors">
          Add product
        </a>
      </div>
    {% else %}
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {% for product in product_list %}
          {% include 'card_product.html' with product=product %}
        {% endfor %}
      </div>
    {% endif %}
...
```
## Urutan prioritas pengambilan CSS selector👆🏻
Misal
```html
<html>
<head>
  <style>
    #demo {color: blue;} 
    .test {color: green;}
    p {color: red;}
  </style>
</head>
<body>

<p id="demo" class="test" style="color: pink;">Hello World!</p>

</body>
</html>
```
Maka prioritas selectorsnya yaitu:
1. Inline style, override semua selectors. Dari contoh diatas: style="color: pink;"
2. Id selectors, #demo {color: blue;}
3. Class selectors, .test {color: green;}
4. Element selectors, p {color: red;}
5. Universal selector dan :where(), * dan where()

## Responsive design💻
Responsive web design (RWD) adalah pendekatan desain web untuk membuat halaman web page dapat ter-render dengan baik di semua ukuran layar dan resolusi dengan tetap mempertahankan good usability. RWD merupakan hal yang penting karena memberikan beberapa benefit diantaranya sebagai berikut.
1. User experience akan meningkat karena ukuran halaman akan menyesuaikan device sehingga user dapat bernavigasi dengan mudah.
2. Web juga akan lebih menjangkau banyak orang, karena tidak semua orang memiliki PC ataupun akan membuka web di PC.
3. Cost effective, karena tidak perlu membangun banyak versi web untuk setiap device.
4. Maintenace lebih mudah, karena tidak perlu mengelola berbagai versi web untuk setiap device.
5. Competitive advantage, menawarkan experience yang seamless antar device.
Aplikasi yang sudah menerapkan responsive design: Instagram
Aplikasi yang belum menerapkan responsive design: SIAK NG

## Margin, border, dan padding🧥
Box model pada CSS pada dasarnya merupakan suatu box yang membungkus setiap elemen HTML dan terdiri atas:

<img width="948" height="400" alt="Screen Shot 2025-09-30 at 19 10 23" src="https://github.com/user-attachments/assets/e27e93e0-ab3f-43c8-860e-5b01b0c39cb5" />
1. Content: isi dari box (tempat terlihatnya teks dan gambar)
2. Padding: mengosongkan area di sekitar konten (transparan)
3. Border: garis tepian yang membungkus konten dan padding-nya
4. Margin: mengosongkan area di sekitar border (transparan)

Contoh implementasinya yaitu
``` css
div {
  width: 320px;
  height: 50px;
  padding: 10px;
  border: 5px solid gray;
  margin: 0;
}
```

## Flex box dan grid layout📦
Flexbox adalah metode layout untuk mengatur item berdasarkan baris ATAU kolom. Grid layout menghadirkan sistem layout grid-based, with rows DAN columns. Flexbox digunakan untuk layout satu dimensi, sedangkan grid layout digunakan untuk layout dua dimensi. Oleh karena itu, Flexbox cocok digunakan untuk membuat layout web yang kompleks. Kedua metode tersebut mempermudah desain struktur layout yang responsif, tanpa menggunakan float atau positioning. 
</details>
