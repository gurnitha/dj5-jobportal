## BUILD JOB PORTAL APP USING DJANGO 5


## 1. PROYEK DAN APLIKASI

#### 1. Membuat lingkungan virtual

        - Menginstal Python dan pip
        - Membuat lingkungan virtual
        - Mengaktifkan lingkungan virtual
        - Menginstal Django

#### 2. Membuat remote repositori dan mengupload file proyek ke remote repositori

        - Membuat akun di Github
        - Membuat repositori baru
        - Upload file proyek ke remote repositori

#### 3. Menginisiasi proyek

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 4. Membuat aplikasi jobs

        new file:   apps/jobs/__init__.py
        new file:   apps/jobs/admin.py
        new file:   apps/jobs/apps.py
        new file:   apps/jobs/migrations/__init__.py
        new file:   apps/jobs/models.py
        new file:   apps/jobs/tests.py
        new file:   apps/jobs/views.py

#### 5. Register aplikasi jobs pada proyek

        modified:   README.md
        modified:   config/settings.py

        Note:

        1. Aplikasi jobs tidak diketahui. 
        Hal itu disebabkan karena kita membuat struktur
        proyek sesuai kebutuhan kita.

        >> ModuleNotFoundError: No module named 'jobs'

#### 6. Membuat path untuk apps

        (venv312513) λ python manage.py check
        System check identified no issues (0 silenced).

#### 7. Halo Dunia!

        modified:   README.md
        new file:   apps/jobs/urls.py
        modified:   apps/jobs/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/jobs/index.html


## 2. DATABASE

#### 1. Membuat MySQL database

        λ mysql -u root
        ...
        mysql>
        mysql> CREATE DATABASE dj5_jobportal;
        Query OK, 1 row affected (0.51 sec)