from pathlib import Path


def create_makefile(project_name: str) -> None:
    """Create a Makefile inside the given project directory"""
    
    makefile_content = """
.PHONY: runserver
runserver:
ifeq ($(port),)
	python manage.py runserver
else
	python manage.py runserver $(port)
endif

.PHONY: superuser
superuser:
	python manage.py createsuperuser

.PHONY: migrations
migrations:
ifeq ($(app),)
	python manage.py makemigrations
else
	python manage.py makemigrations $(app)
endif

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: shell
shell:
	python manage.py shell

.PHONY: dbshell
dbshell:
	python manage.py dbshell
    """
    
    project_path = Path(project_name)
    makefile_path = project_path / 'Makefile'
    
    try:
        makefile_path.write_text(makefile_content.strip())
    except Exception as e:
        print(f"An error occurred while creating the Makefile: {e}")