from pathlib import Path

def remove_directory_if_empty(directory: Path) -> None:
    """Remove the directory if it is empty."""
    if not any(directory.iterdir()):
        directory.rmdir()
