from pathlib import Path

def initialize_settings_files(settings_dir: Path) -> None:
    """Initialize settings files."""
    filenames = ['__init__.py', 'local.py', 'production.py', '.env']
    for filename in filenames:
        file_path = settings_dir / filename
        file_path.touch()

    env_content = """
SECRET_KEY=
DEBUG=True

# Email Settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_USE_TLS= True
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
    """

    (settings_dir / '.env').write_text(env_content.strip())

    local_py_content = "from .base import *\n"
    (settings_dir / 'local.py').write_text(local_py_content.strip())

    production_py_content = "from .base import *\n"
    (settings_dir / 'production.py').write_text(production_py_content.strip())
