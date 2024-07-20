# Django Project Setup Script

## Overview

This Python script automates the setup of a Django project with a specified structure. It creates a Django project, moves essential files, initializes settings, and sets up a Makefile with common Django commands.

---
## Features

- **Project Initialization**: Automatically creates a Django project with your specified name.
- **Settings Management**: 
  - Relocates and renames `settings.py` to `core/settings/base.py`.
  - Initializes additional settings files (`local.py`, `production.py`, and `.env`) for environment-specific configurations.
- **App Creation**: 
  - Creates a Django app with the specified name.
  - Strategically places the app within the `core/apps` directory.
- **Directory Structure**: 
  - Sets up essential directories including `templates`, `static`, and `media`.
  - Creates a default `base.html` template and an `app_name/home.html` template for your app.
- **URL Configuration**: 
  - Updates the root `urls.py` to seamlessly integrate the project and app URLs.
  - Adds necessary URL patterns for the created app.
- **Makefile Generation**: Produces a `Makefile` that includes common Django commands for streamlined project management.
- **Static and Media Files**: 
  - Sets up directories for static and media files.
  - Configures `settings.py` to properly handle static and media files.
- **ASGI and WSGI Configuration**: 
  - Updates `asgi.py` and `wsgi.py` to use the new settings module.
---

This expanded features list provides a comprehensive overview of the functionalities your Django project setup script offers, highlighting its robustness and ease of use.

## Requirements

- Python 3.x
- Django 5.x

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script to create a Django project:**

    ```bash
    python main.py <project_name> <app_name>
    ```

   Replace `<project_name>` with the desired name of your Django project and `<app_name>` with the name of the Django app you want to create.

2. **Navigate to your project directory:**

    ```bash
    cd <project_name>
    ```

3. **Use the Makefile to manage your Django project:**

    - **Run the development server:**

      ```bash
      make runserver
      ```

    - **Create a superuser:**

      ```bash
      make superuser
      ```

    - **Create migrations for all apps or a specific app:**

      ```bash
      make migrations       # For all apps
      make migrations app=<app_name>  # For a specific app
      ```

    - **Apply migrations:**

      ```bash
      make migrate
      ```

    - **Open the Django shell:**

      ```bash
      make shell
      ```

    - **Open the database shell:**

      ```bash
      make dbshell
      ```

## Notes

- Before starting the development server, ensure you read `SETUP.md` to configure `base.py` properly.
- Ensure that Django is installed and available in your environment.
- The `Makefile` assumes you have `make` installed on your system. If not, you can install it using your package manager.
- I have also included a `.gitignore` file designed specifically for Django projects. This file helps you keep unnecessary files and directories out of your version control, ensuring a cleaner and more efficient repository.


