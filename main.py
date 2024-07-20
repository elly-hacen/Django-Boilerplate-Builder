import atexit
import argparse
from rich.text import Text
from rich.panel import Panel
from rich.console import Console
from utils.django_setup import create_django_project


console = Console()

def exit_handler():
    """Function to be called on program exit to print creator details."""
    creator_info = Text.from_markup(
        """
        [bold blue]:star: Django Boilerplate Builder :star:[/bold blue]
        
        [bold cyan]Created by:[/bold cyan] [bold yellow]Ali Hassan[/bold yellow]
        
        [bold cyan]GitHub:[/bold cyan] [link=https://github.com/elly-hacen]https://github.com/elly-hacen[/link]
        [bold cyan]LinkedIn:[/bold cyan] [link=https://www.linkedin.com/in/elly-hacen]https://www.linkedin.com/in/elly-hacen[/link]
        
        
        [bold cyan]Version:[/bold cyan] [bold yellow]1.0[/bold yellow]
        """
    )
    # Print the formatted text inside a panel
    console.print(Panel(creator_info, title="Django Boilerplate Builder", title_align="center", border_style="bold magenta"))


atexit.register(exit_handler)

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Create a Django project with a custom structure")

    # Add the arguments
    parser.add_argument(
        'project_name',
        type=str,
        help='Name of the Django project'
    )

    parser.add_argument(
        'app_name',
        type=str,
        help='Name of the Django app'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Create the Django project and app with the parsed arguments
    create_django_project(args.project_name, args.app_name)
   