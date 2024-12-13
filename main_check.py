import os

for dirpath, dirnames, filenames in os.walk(r'C:\Users\vpc\PycharmProjects'):
    for filename in filenames:
        full_filename = os.path.join(dirpath, filename)
        if filename.endswith('text_to_matrix.py') and 'venv' not in full_filename \
                and 'virtualenv' not in full_filename:
            inf = open(full_filename)
            main_check = False
            try:
                for line in inf:
                    if "if __name__ == '__main__':" in line:
                        main_check = True
                        break
            except UnicodeDecodeError:
                # print('unicode error', full_filename)
                pass
            if not main_check:
                print(full_filename)
            inf.close()

if __name__ == '__main__':
    pass
