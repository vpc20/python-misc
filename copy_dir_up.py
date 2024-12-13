import os
import shutil

path = r"C:\Users\vpc\Downloads\network-penetration-testing-python-kali-linux"
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('text_to_matrix.py'):
            shutil.copy(os.path.join(dirpath, filename), os.path.join(path, filename))
