import os.path


def read_file(path_parts, mode='r'):
    with open(os.path.join(path_parts), mode) as file:
        return file.read()
