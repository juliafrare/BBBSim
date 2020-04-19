import os

def file_fullpath(file_name):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    print(file_dir)
    fullpath = os.path.join(file_dir, file_name)
    return fullpath