import os


def find_hypen_underscore(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if '-' in filename or '_' in filename:
                print(filename)


find_hypen_underscore(r'C:/Users/vpc/Music')

