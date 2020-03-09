import os
import os.path

def check_exist_or_create_file(fullpath):
    directory, filename = os.path.split(fullpath)
    if not filename:
        raise Exception( f"There is no file specified in path {fullpath}.")

    if os.path.exists(fullpath):
        return

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(fullpath, 'w'):
        pass