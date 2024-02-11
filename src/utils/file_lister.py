# import required package 🚀
from re import findall
from os import walk


def file_lister(target: str, with_path=False):
    p_list, f_list = [], []
    for root, _, files in walk(target):
        for name in sorted(files, key=lambda s: int(findall(r"\d+", s)[0])):
            p_list.append(f"{root}/{name}")
            f_list.append(name)
    return (p_list, f_list) if with_path else f_list
