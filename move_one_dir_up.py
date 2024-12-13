import os
import shutil

for dirpath, dirnames, filenames in os.walk(r"c:\temp"):
    for dirname in dirnames:
        for dirpath1, dirnames1, filenames1 in os.walk(os.path.join(dirpath, dirname)):
            for filename in filenames1:
                full_filename = os.path.join(dirpath1, filename)
                new_name = os.path.join(dirpath, filename)
                print(f'Moving {filename}...')
                shutil.move(full_filename, new_name)  # move one dir up
                if len(os.listdir(dirpath1)) == 0:
                    print(f'Remove dir {dirpath1}...')
                    os.rmdir(dirpath1)  # remove dir
