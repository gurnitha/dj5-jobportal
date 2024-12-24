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

#### 6. Membuat file migrasi dan membuat tabel

        (venv312513) λ python manage.py makemigrations
        Migrations for 'users':
          apps\users\migrations\0001_initial.py
            + Create model CustomUser

        (venv312513) λ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions, users
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0001_initial... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying users.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying sessions.0001_initial... OK

        C:\Users\ING\Desktop\workspace\dj5-jobportal-volkan-altis\jobportal(main -> origin)
        (venv312513) λ python manage.py createsuperuser
        Email address: admin@mail.com
        Password:
        Password (again):
        The password is too similar to the email address.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.

        modified:   README.md
        modified:   apps/users/admin.py
        new file:   apps/users/migrations/0001_initial.py
        new file:   apps/users/migrations/0002_alter_customuser_is_superuser.py
        modified:   apps/users/models.py

        :)

#### 7. Memodifikasi tampilan CustomUser pada admin panel

        modified:   README.md
        modified:   apps/users/admin.py


## 4. TEMPLATES

#### 1. Membuat path untuk file statis

        modified:   README.md
        modified:   config/settings.py
        new file:   static/css/.DS_Store
        ...
        new file:   static/scss/style.scss
        new file:   static/starter.css

#### 2. Mengisi html template untuk laman home

        modified:   README.md
        modified:   templates/jobs/index.html

#### 3. Load file statis pada template

        modified:   README.md
        modified:   templates/jobs/index.html

#### 4. Membuat base template dan menerapkan template inheritance

        modified:   README.md
        new file:   templates/base.html
        new file:   templates/components/01_navbar.html
        new file:   templates/components/02_hero.html
        new file:   templates/components/03_company_ads_1.html
        new file:   templates/components/04_job_category.html
        new file:   templates/components/05_job_recent.html
        new file:   templates/components/06_company_ads_2.html
        new file:   templates/components/07_happy_client.html
        new file:   templates/components/08_blog_recent.html
        new file:   templates/components/09_news_letter.html
        new file:   templates/components/10_footer.html
        new file:   templates/components/11_loader.html
        modified:   templates/jobs/index.html

#### 5. Membuat page title menggunakan block.super

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/jobs/index.html

#### 6. Membuat blog app dan mendaftarkannya pada proyek

        modified:   README.md
        new file:   apps/blog/__init__.py
        new file:   apps/blog/admin.py
        new file:   apps/blog/apps.py
        new file:   apps/blog/migrations/__init__.py
        new file:   apps/blog/models.py
        new file:   apps/blog/tests.py
        new file:   apps/blog/views.py
        modified:   config/settings.py

#### 7. Membuat laman blog posts_list

        modified:   README.md
        new file:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   config/urls.py
        new file:   templates/blog/posts_list.html
        modified:   templates/components/01_navbar.html

#### 8. Membuat laman blog post_single

        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        new file:   templates/blog/post_single.html
        modified:   templates/blog/posts_list.html
        modified:   templates/components/01_navbar.html

#### 9. Membuat laman jobs_list

        modified:   README.md
        modified:   apps/jobs/urls.py
        modified:   apps/jobs/views.py
        modified:   templates/components/01_navbar.html
        new file:   templates/jobs/jobs_list.html

#### 10. Membuat laman job_create

        modified:   README.md
        modified:   apps/jobs/urls.py
        modified:   apps/jobs/views.py
        modified:   templates/components/01_navbar.html
        new file:   templates/jobs/job_create.html
        modified:   templates/jobs/jobs_list.html