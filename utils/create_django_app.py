import os
import shutil
import subprocess
from pathlib import Path

def create_django_app(project_name: str, app_name: str) -> None:
    """Create the Django app inside core/apps"""
    
    manage_py_file_location = os.path.join(os.getcwd(), project_name)
    os.chdir(manage_py_file_location)
    
    app_dest_dir = Path('core') / 'apps' / app_name

    try:
        subprocess.run(['python', 'manage.py', 'startapp', app_name], check=True)

        app_source_dir = Path(app_name)
        
        shutil.move(str(app_source_dir), str(app_dest_dir))

    except subprocess.CalledProcessError as e:
        print(f"Error creating Django app: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    
    filenames = ['forms.py', 'urls.py', 'tests.py', 'context_processor.py']
    for filename in filenames:
        file_path = app_dest_dir / filename
        file_path.touch()

    forms_py_content = "from django import forms\n"
    (app_dest_dir / 'forms.py').write_text(forms_py_content.strip())

    tests_py_content = "from django.test import TestCase\n"
    (app_dest_dir / 'tests.py').write_text(tests_py_content.strip())

    urls_py_content = f"""
from django.urls import path
from core.apps.{app_name} import views

app_name = '{app_name}'

urlpatterns = [
    path('', views.home, name='{app_name}_home'),
]
    """
    (app_dest_dir / 'urls.py').write_text(urls_py_content.strip())

    views_py_content = f"""
from django.shortcuts import render


def home(request):
    return render(request, '{app_name}/home.html')
    """
    (app_dest_dir / 'views.py').write_text(views_py_content.strip())

    apps_py_content = f"""
from django.apps import AppConfig


class QuizzesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.{app_name}'
    """
    (app_dest_dir / 'apps.py').write_text(apps_py_content.strip())
