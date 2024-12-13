import os

for dirpath, dirnames, filenames in os.walk(r'C:\Users\vpc\Videos\HDpiano'):
    # print(dirpath, dirnames, filenames)
    fileset = set([filename[:filename.find('-')] for filename in filenames])
    for file in sorted(fileset):
        print(file)
    print(len(fileset))

