-- Step by step implementasi checklist --

Inisiasi
1. Membuat direktori luluorange, membuat virtual environment pada direktori tersebut dengan python3 -m venv env, dan mengaktifkannya dengan source env/bin/activate
2. Membuat requirements.txt dan menginstall dependencies yang ada di file tersebut dengan pip install -r requirements.txt
3. Membuat proyek django dengan perintah django-admin startproject luluorange .
4. Membuat file .env dan .env.prod untuk konfigurasi environment variables
5. Membuat file .gitignore untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git
5. Membuat aplikasi main dalam proyek luluorange dengan python manage.py startapp main
6. Memodifikasi settings.py seperti pada tutorial 0 (import load_dotenv, tambah allowed_hosts, konfigurasi database, konfigurasi PRODUCTION, tambah installed_apps dengan 'main') 


Membuat models, views, dan template
7. Memodifikasi berkas models.py pada aplikasi main, membuat model dengan nama Product, dan memasukkan atribut-atribut wajib yang tertera pada dokumen soal
8. Lakukan migrasi model dengan python manage.py migrate
9. Menambahkan fungsi show_main pada file views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
10. Membuat direktori templates pada aplikasi main lalu membuat file main.html yang berisi nama aplikasi, nama, dan kelas menggunakan sintaks Django {{ app }}, {{ name }} dan {{ class }}, agar bisa menampilkan nilai dari variabel yang telah didefinisikan dalam context pada fungsi show_main

Melakukan routing URL
11. Untuk mengonfigurasi routing URL aplikasi main, buat urls.py pada aplikasi main dan mengisinya dengan URL pattern yang kita kehendaki
12. Untuk mengonfigurasi routing URL proyek, buka urls.py pada direktori proyek dan mengisinya dengan URL pattern yang kita kehendaki (Menggunakan include('main.urls') untuk mengimpor pola rute URL dari aplikasi main ke dalam berkas urls.py level proyek)
13. Menjalankan server dengan python3 manage.py runserver untuk melihat apakah web sudah dapat berjalan dengan baik

Deployment ke PWS
14. Buka PWS dan create new project, lalu copy paste isi file .env.prod ke tab environs pada project yang baru dibuat
15. Update allowed-host pada file settings.py (menambahkan URL Deployment PWS "rasyad-zulham-luluorange.pbp.cs.ui.ac.id")
16. Jalankan perintah yang diberikan ketika membuat project baru, lalu masukkan username dan password yang sudah diberikan juga saat membuat project baru
17. Apabila status proyek 'running', maka bisa klik view project untuk melihat project dari link yang bisa dilihat oleh orang lain

-- Request-Response Cycle --
<img width="1130" height="635" alt="Screen Shot 2025-09-08 at 21 02 44" src="https://github.com/user-attachments/assets/cec128c2-93e2-4a98-8775-afdf70b52a8b" />
