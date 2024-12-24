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

#### 2. Menghubungkan proyek dengan database

        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'dj5_jobportal',
            'USER': 'root',
            'PASSWORD': '',
            'HOST':'localhost',
            'PORT':'3306',
            }
        }

        django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
        Did you install mysqlclient?

        modified:   README.md
        modified:   config/settings.py

#### 3. Menginstal mysqlclient

        (venv312513) λ pip install mysqlclient
        ...
        Successfully installed mysqlclient-2.2.6

        # Testing
        (venv312513) λ python manage.py runserver
        ...
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


## 3. MODELS

#### 1. Membuat users app

        modified:   README.md
        new file:   apps/users/__init__.py
        new file:   apps/users/admin.py
        new file:   apps/users/apps.py
        new file:   apps/users/migrations/__init__.py
        new file:   apps/users/models.py
        new file:   apps/users/tests.py
        new file:   apps/users/views.py

#### 2. Register users app pada proyek

        modified:   README.md
        modified:   config/settings.py

#### 3. Membuat CustomUserManager

        modified:   README.md
        modified:   apps/users/models.py

#### 4. Membuat CustomUser

        modified:   README.md
        modified:   apps/users/models.py

#### 5. Mendaftarkan CustomUser pada settings.py sebagai default model

        modified:   README.md
        modified:   config/settings.py