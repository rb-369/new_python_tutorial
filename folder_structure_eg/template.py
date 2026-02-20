import os
from pathlib import Path

# Define project name
project_name = "your_project_name"

# Define the structure to create
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "main.py",
    "requirements.txt",
    "setup.py"
]

# Generate directory structure and empty files
for filepath in list_of_files:
    path = Path(filepath)
    filedir, filename = os.path.split(path)
    if filedir:
        os.makedirs(filedir, exist_ok=True)
    if not path.exists() or path.stat().st_size == 0:
        with open(path, "w") as f:
            pass
