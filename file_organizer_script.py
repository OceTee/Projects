#!/usr/bin/env python3
"""
File Organizer Script

This script organizes files in a specified directory by moving them into
folders based on their file extensions. It creates folders for each unique
extension and moves the corresponding files into them.

Usage:
    python file_organizer_script.py

The script will prompt for the directory path to organize.
"""

import os
import shutil
from pathlib import Path


def get_directory_path():
    """
    Prompt the user for the directory path to organize.

    Returns:
        Path: The path to the directory to organize.
    """
    while True:
        path_str = input("Enter the path to the directory you want to organize: ").strip()
        path = Path(path_str)

        if path.exists() and path.is_dir():
            return path
        else:
            print("Invalid directory path. Please try again.")


def organize_files(directory_path):
    """
    Organize files in the given directory by their extensions.

    Args:
        directory_path (Path): The path to the directory to organize.
    """
    # Get all files in the directory (not subdirectories)
    files = [f for f in directory_path.iterdir() if f.is_file()]

    if not files:
        print("No files found in the directory.")
        return

    # Group files by extension
    extension_groups = {}
    for file_path in files:
        extension = file_path.suffix.lower()  # Get extension in lowercase
        if extension:  # Skip files without extensions
            if extension not in extension_groups:
                extension_groups[extension] = []
            extension_groups[extension].append(file_path)

    # Create folders and move files
    for extension, file_list in extension_groups.items():
        # Create folder name (remove the leading dot from extension)
        folder_name = extension[1:].upper() + "_Files"
        folder_path = directory_path / folder_name

        # Create the folder if it doesn't exist
        folder_path.mkdir(exist_ok=True)

        # Move files to the folder
        for file_path in file_list:
            new_path = folder_path / file_path.name
            shutil.move(str(file_path), str(new_path))
            print(f"Moved {file_path.name} to {folder_name}/")

    print(f"\nOrganization complete! Files have been moved into {len(extension_groups)} folders.")


def main():
    """
    Main function to run the file organizer script.
    """
    print("Welcome to the File Organizer Script!")
    print("This script will organize files in a directory by their extensions.\n")

    directory_path = get_directory_path()
    print(f"Organizing files in: {directory_path}\n")

    organize_files(directory_path)

    print("\nThank you for using the File Organizer Script!")


if __name__ == "__main__":
    main()