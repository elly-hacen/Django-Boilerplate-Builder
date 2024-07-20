from pathlib import Path

def update_manage_py(project_name: str) -> None:
    manage_py_path = Path(project_name) / 'manage.py'
    
    manage_py_content = """\
#!/usr/bin/env python
\"\"\"Django's command-line utility for administrative tasks.\"\"\"
import os
import sys
from core.settings import base


def main():
    \"\"\"Run administrative tasks.\"\"\"
    if base.DEBUG:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.local')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.production')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
"""

    manage_py_path.write_text(manage_py_content.strip())