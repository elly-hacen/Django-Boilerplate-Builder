from pathlib import Path

def update_root_urls(project_name: str, app_name: str) -> None:
    """Update core/urls.py with URL patterns."""
    
    root_urls_path = Path(project_name) / 'core' / 'urls.py'
    
    urls_py_content = f"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.apps.{app_name}.urls', namespace='{app_name}')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" 
    root_urls_path.write_text(urls_py_content.strip())