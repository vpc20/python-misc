import os


def rename_file(path):
    for dirpath, dirnames, filenames in os.walk(path):
        dirnames.clear()
        for filename in filenames:
            old_name = os.path.join(dirpath, filename)
            ext = os.path.splitext(filename)[-1]
            split_name = filename.split('-')
            new_name = os.path.join(dirpath, split_name[1].strip() + ext)
            print(old_name)
            print(new_name)
            # os.rename(old_name, new_name)


rename_file(r'C:\temp')
