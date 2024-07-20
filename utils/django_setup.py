import subprocess
from pathlib import Path
from .create_directories import create_directories, setup_templates_and_static
from .move_files import move_files
from .initialize_settings_files import initialize_settings_files
from .remove_directory_if_empty import remove_directory_if_empty
from .update_asgi_and_wsgi_files import update_asgi_and_wsgi_files
from .create_django_app import create_django_app
from .update_manage_py import update_manage_py
from .update_root_urls import update_root_urls
from .create_makefile import create_makefile

def create_django_project(project_name: str, app_name: str) -> None:
    """Create a Django project with the given project and app name."""
    try:
        subprocess.run(['django-admin', 'startproject', project_name], check=True)

        base_dir = Path(project_name)
        core_dir = base_dir / 'core'
        project_dir = base_dir / project_name
        settings_dir = core_dir / 'settings'
        app_dir = core_dir / 'apps'
        templates_dir = base_dir / 'templates'
        static_dir = base_dir / 'static'
        media_dir = base_dir / 'media'

        directories = [core_dir, app_dir, settings_dir, templates_dir, static_dir, media_dir]
        create_directories(directories)

        move_files(
            source_dir=project_dir,
            destination_dir=core_dir,
            exclude_file='settings.py',
            new_filename='base.py',
            special_move={'destination': settings_dir}
        )

        initialize_settings_files(settings_dir)
        remove_directory_if_empty(project_dir)
        
        update_manage_py(project_name)
        update_root_urls(project_name, app_name)
        
        create_makefile(project_name)
        
        setup_templates_and_static(project_name, app_name)
        
        update_asgi_and_wsgi_files(project_name)
        
        
    except subprocess.CalledProcessError as e:
        print(f"Error creating Django project: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    create_django_app(project_name, app_name)
    
    
