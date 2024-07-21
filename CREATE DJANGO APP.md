# How to Create a Django App

This guide will walk you through the steps to create a new Django app within your Django project.

## Steps to Create a Django App

1. **Navigate to Your Project Directory**

   Open your terminal or command prompt and navigate to the root directory of your Django project:

   ```bash
   cd path/to/your/project
   ```

2. **Create a New Django App**

   Use the `startapp` command to create a new app. Replace `your_app_name` with the desired name of your app:

   ```bash
   python manage.py startapp your_app_name
   ```

   This will create a new directory named `your_app_name` with the following structure:

   ```
   your_app_name/
       __init__.py
       admin.py
       apps.py
       models.py
       tests.py
       views.py
   ```

3. **Move the App Directory**

   Move the app directory to `core/apps/your_app_name`:

   ```bash
   mv your_app_name core/apps/your_app_name
   ```

4. **Update `apps.py`**

   Open `core/apps/your_app_name/apps.py` and update the `AppConfig` class:
    - You just have to add `core.apps` in name attribute
   ```python
   from django.apps import AppConfig

   class YourAppNameConfig(AppConfig):
       default_auto_field = 'django.db.models.BigAutoField'
       name = 'core.apps.your_app_name'
   ```

5. **Register the App with the Project**

   Open the `settings.py` file in your project’s main directory (e.g., `project_name/settings.py`) and add your new app to the `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [
       ...
       'core.apps.your_app_name',
   ]
   ```

7. **Configure URLs**

   Create a `urls.py` file in your app directory (`core/apps/your_app_name/urls.py`) and define URL patterns:

   ```python
   from django.urls import path
   from core.apps.your_app_name import views

   app_name = 'your_app_name'

   urlpatterns = [
       path('', views.index, name='index'),
   ]
   ```

   Include these URLs in the project's main `urls.py` file (`project_name/urls.py`):

   ```python
   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('your_app_name/', include('core.apps.your_app_name.urls', namespace='your_app_name')),
   ]
   ```

6. **Create Migrations**

   Create migrations for all apps or a specific app:

   ```bash
   python manage.py makemigrations  # For all apps
   python manage.py makemigrations your_app_name  # For a specific app
   ```

10. **Run the Development Server**

    Start the Django development server to see your app in action:

    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/your_app_name/` in your browser to view your new app.

