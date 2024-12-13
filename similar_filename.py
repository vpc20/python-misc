import os


# def similar_filenames(path):
#     try:
#         dir_list = os.listdir(path)
#     except WindowsError:
#         raise OSError('Error in reading directory')
#
#     prev_dir_entry = ''
#     for dir_entry in dir_list:
#         complete_dir_entry = os.path.join(path, dir_entry)
#         if os.path.isfile(complete_dir_entry):
#             if dir_entry[:11] == prev_dir_entry[:11]:
#                 print('\n' + prev_dir_entry)
#                 print(dir_entry)
#             else:
#                 prev_dir_entry = dir_entry


def similar_filenames(path):
    prev_filename = ''
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename[:11] == prev_filename[:11]:
                print('')
                print(dirpath)
                print(prev_filename)
                print(filename)
            else:
                prev_filename = filename
        dirnames.clear()  # do not go to sub-directories


similar_filenames(r'C:\Users\vpc\Pictures')
