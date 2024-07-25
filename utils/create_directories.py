from pathlib import Path
from typing import List

def create_directories(paths: List[Path]) -> None:
    """Create directories if they do not exist."""
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)
        

def initialize_apps_dir(app_dir: str):
  project_path = Path(app_dir)
  init_file_path = project_path / '__init__.py'
  if not init_file_path.exists():
        init_file_path.touch()
  
   

def setup_templates_and_static(project_name: str, app_name: str) -> None:
    """Create the templates and static directory structure for a Django project."""
    
    project_path = Path(project_name)

    # Create templates directory with app_name subdirectory
    templates_path = project_path / 'templates' / app_name
    templates_path.mkdir(parents=True, exist_ok=True)

    # Create home.html inside the templates/app_name directory
    home_html_path = templates_path / 'home.html'
    home_html_path.touch()

    # Create static directory with assets, css, and js subdirectories
    static_path = project_path / 'static'
    assets_path = static_path / 'assets'
    css_path = static_path / 'css'
    js_path = static_path / 'js'

    create_directories([assets_path, css_path, js_path])

    # Create style.css and script.js
    (css_path / 'style.css').touch()
    (js_path / 'script.js').touch()


    base_html_path = project_path / 'templates' / 'base.html'
    
    base_html_content = f"""
{{% load static %}}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>
            {{% block title %}} {app_name} {{% endblock %}}
        </title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link
            href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;1,300&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900&display=swap"
            rel="stylesheet">
   
        {{#        <-- fav icon -->     #}}
        <link rel="shortcut icon" href="{{% static 'assets/favicon/logo.png' %}}" type="image/x-icon">
    
        <link rel="stylesheet" href="{{% static 'css/style.css' %}}">
        <link rel="stylesheet" href="{{% block stylesheet %}}{{% endblock %}}">
    </head>
    <body>

        {{% block content %}}
            
        {{% endblock %}} 
    
    </body>

</html>"""
    base_html_path.write_text(base_html_content.strip())
    
    home_html_content = f"""
{{% load static %}} 
{{% block content %}}

<style>
  body {{
    font-family: Arial, sans-serif;
    background-color: #D9AFD9;
    background-image: linear-gradient(0deg, #D9AFD9 0%, #97D9E1 100%);
    
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }}

  .container {{
    background-color: #f1fbea;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    text-align: center;
    max-width: 600px; /* Increased max-width for better alignment */
    width: 100%;
    box-sizing: border-box; /* Ensures padding is included in width */
    margin: 0 15px;
  }}

  h1 {{
    color: #2e2e2e;
    margin-bottom: 20px;
    font-size: 2.5em;
    font-weight: bold;
    line-height: 1.2; /* Adjusted for better spacing */
  }}

  p {{
    font-size: 1.2em;
    color: black;
    margin: 0 auto 30px auto; /* Center align with auto margins */
    line-height: 1.8; /* Increased line-height for better readability */
    text-align: center;
    max-width: 90%; /* Prevents text from stretching too wide */
  }}

  .links {{
    margin-top: 20px;
  }}

  .links a {{
    display: inline-block;
    text-decoration: none;
    color: #ffffff;
    background: linear-gradient(to right, #6a11cb, #2575fc);
    padding: 12px 24px;
    border-radius: 25px;
    font-size: 1.2em;
    font-weight: 600;
    transition: background 0.3s, transform 0.3s;
    margin: 0 15px;
  }}

  .links a:hover {{
    background: linear-gradient(to right, #2575fc, #6a11cb);
    transform: scale(1.05);
  }}
</style>

<div class="container">
  <h1>About Me</h1>
  <p>
    I am a Python developer specializing in Django for backend development. I am
    passionate about learning and working with Linux (I use Arch Linux, by the
    way). Currently, I am a student at the University of Agriculture Faisalabad,
    pursuing a Bachelor's degree in Information Technology.
  </p>
  <div class="links">
    <a href="https://www.linkedin.com/in/elly-hacen" target="_blank">LinkedIn</a>
    <a href="https://github.com/elly-hacen" target="_blank">GitHub</a>
  </div>
</div>

{{% endblock %}}

"""

    home_html_path.write_text(home_html_content.strip())
