import os
import platform
from pathlib import Path
import warnings

# This script removes all of the screenshots in Screenshots folder.

def get_screenshots_dir(operating_system, home_dir): 
    screenshots_path = home_dir / "Pictures" / "Screenshots"

    if operating_system == 'Linux':
        if os.path.exists(screenshots_path):
            return screenshots_path
    elif operating_system == "Windows":
        if os.path.exists(screenshots_path):
            return screenshots_path

    return "" 

def main():
    operating_system = platform.system()
    home_dir = Path.home()
    screenshots_dir = get_screenshots_dir(operating_system, home_dir)

    if screenshots_dir != "":
        for file in Path.iterdir(Path(screenshots_dir)):
            try:  
                file.unlink()
            except FileNotFoundError as e:
                warnings.warn(f"Unable to unlink the '{e.filename}' file because it doesn't exists. Skipped")
                continue

if __name__ == "__main__":
    main()
