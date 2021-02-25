import re
import requests
import os.path


def download(url, name_dir):
    r = requests.get(url)
    file_name = get_full_name(url, name_dir)
    with open(file_name, 'w') as file:
        file.write(r.text)
    return file_name


def get_full_name(url, directory):
    crop_schema = re.sub(r'http[s]?://', '', url)
    words = list(re.sub(r'[\W_]', ' ', crop_schema).rstrip().split(' '))
    file_name = f"{'-'.join(words)}.html"
    full_path = os.path.join(directory, file_name)
    return full_path
