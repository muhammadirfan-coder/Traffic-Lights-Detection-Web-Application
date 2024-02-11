from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

print("Absolute PaTH: ",file_path)

root_path = file_path.parent
print("Root Directory:",root_path)

if root_path not in sys.path:
    sys.path.append(str(root_path))

ROOT = root_path.relative_to(Path.cwd())

print("cwd: ",ROOT)



IMAGES_DIR = ROOT / 'images'

print(IMAGES_DIR)