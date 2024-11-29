import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    """
    Back up files from the source directory to the destination directory.
    Ensures uniqueness by appending a timestamp to file names if they already exist.

    :param source_dir: Path to the source directory.
    :param dest_dir: Path to the destination directory.
    """
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Check if destination directory exists, create if it doesn't
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            print(f"Destination directory '{dest_dir}' created.")

        # Iterate through files in the source directory
        for file_name in os.listdir(source_dir):
            source_file = os.path.join(source_dir, file_name)

            # Skip directories, process files only
            if os.path.isfile(source_file):
                dest_file = os.path.join(dest_dir, file_name)

                # Check if a file with the same name exists in the destination
                if os.path.exists(dest_file):
                    # Append timestamp to the file name
                    base_name, ext = os.path.splitext(file_name)
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    dest_file = os.path.join(dest_dir, f"{base_name}_{timestamp}{ext}")

                # Copy file to destination
                shutil.copy2(source_file, dest_file)
                print(f"Copied '{source_file}' to '{dest_file}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        backup_files(source_dir, dest_dir)
