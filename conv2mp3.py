import os


def conv2mp3(filepath):
    for dirpath, dirnames, filenames in os.walk(filepath):
        print(dirpath, dirnames, filenames)
        for filename in filenames:
            fname, ext = os.path.splitext(filename)
            if ext in ('.webm', '.mp4'):
                command = f'ffmpeg -i {filename} {fname}.mp3'
                print(command)
        dirnames.clear()  # do not perform dir walk recursively


conv2mp3(os.curdir)

