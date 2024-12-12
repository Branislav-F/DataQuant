import os

def create_project_structure():
    structure = {
        "devices": ["rigol_dm3068.py"],              # Subfolder with specific files
        "measurements": ["current.py", "voltage.py"], # Subfolder with specific files
        "storage": ["influxdb_storage.py"],          # Subfolder with specific files
        ".": ["main.py", "requirements.txt", "README.md"]  # Files in the current directory
    }

    base_path = os.getcwd()  # Current working directory is `DataQuant`

    for folder, files in structure.items():
        if folder != ".":  # Create subfolders
            folder_path = os.path.join(base_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            for file in files:
                open(os.path.join(folder_path, file), 'w').close()  # Create empty files in subfolder
        else:  # Create files in the current directory
            for file in files:
                open(os.path.join(base_path, file), 'w').close()  # Create empty files in the root

    print(f"Project structure created in {base_path}")

if __name__ == "__main__":
    create_project_structure()

