from pathlib import Path


def parse_folder(path):
    file_list = []
    dir_list = []
    for item in path.iterdir():
        if item.is_file():
            file_list.append(str(item.name))
        elif item.is_dir():
            dir_list.append(str(item.name))
    return (file_list, dir_list)
