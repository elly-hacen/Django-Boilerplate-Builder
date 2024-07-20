import shutil
from pathlib import Path

def move_files(source_dir: Path, destination_dir: Path, exclude_file: str, new_filename: str, special_move: dict) -> None:
    """Move files matching the pattern to the destination directory."""
    for file_path in source_dir.iterdir():
        if file_path.name == exclude_file:
            shutil.move(file_path, special_move.get('destination') / new_filename)
        elif file_path.is_file():
            shutil.move(file_path, destination_dir / file_path.name)
