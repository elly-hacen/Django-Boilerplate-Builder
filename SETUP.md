## base.py Configuration Instructions

### BASE_DIR Setup
Ensure that your `BASE_DIR` is set correctly:
```python
BASE_DIR = Path(__file__).resolve().parent.parent.parent
```

### Environment Variables
As we are using `.env` files, add this configuration:
```python
import environ

env = environ.Env()
env.read_env()
```
Now, you can load environment variables like this:
```python
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')
```
Make sure you have installed the `python-environ` package.

### INSTALLED_APPS
Add your app in `INSTALLED_APPS` in `core/settings/base.py`.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # app_name goes here
    'core.apps.app_name',
]
```

### Templates Configuration
In the `TEMPLATES` list, add this line:
```python
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

### Custom User Model
If you are using a custom user model, add this:
```python
AUTH_USER_MODEL = 'app_name.YourCustomUserModelName'
```

### URL Configuration
Change this in `core/settings/base.py`:
From:
```python
ROOT_URLCONF = 'hello.urls'
```
To:
```python
ROOT_URLCONF = 'core.urls'
```

### WSGI Configuration
Change this in `core/settings/base.py`:
From:
```python
WSGI_APPLICATION = 'hello.wsgi.application'
```
To:
```python
WSGI_APPLICATION = 'core.wsgi.application'
```

### Static and Media Files Configuration
Add these configurations for static and media files:
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Email Authentication Configuration
If you're using email authentication, add these settings:
```python
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
```