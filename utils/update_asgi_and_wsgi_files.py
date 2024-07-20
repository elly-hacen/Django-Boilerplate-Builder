from pathlib import Path

def update_asgi_and_wsgi_files(project_name: str) -> None:
    """Update both asgi.py and wsgi.py files inside core/"""
    
    asgi_file_path = Path(project_name) / 'core' / 'asgi.py'
    wsgi_file_path = Path(project_name) / 'core' / 'wsgi.py'
    
    asgi_content = """
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

application = get_asgi_application()
"""
    

    wsgi_content = """
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

application = get_wsgi_application()
"""

    asgi_file_path.write_text(asgi_content.strip())
    wsgi_file_path.write_text(wsgi_content.strip())

