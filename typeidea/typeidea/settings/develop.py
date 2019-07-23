from .base import * # NOQA
# NOQA的作用是，告诉PEP 8规范工具，这里不需要检测


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        # 'USER': '30476',
        # 'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'TEST': {
            'NAME': 'mytestdatabase',
        }
    }
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True