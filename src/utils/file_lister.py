# import required package 🚀
from re import findall
from os import walk


def file_lister(target, with_path=False):
    # initialize lists for path and file list
    p_list, f_list = [], []

    # walk through the directory
    for root, _, files in walk(target):
        # sort files by number in file name
        for name in sorted(files, key=lambda s: int(findall(r"\d+", s)[0])):
            # add full path to p_list
            p_list.append(f"{root}/{name}")
            # add just filename to f_list
            f_list.append(name)
    # return tuple of list if with_path is true, otherwise return only p_list
    return (p_list, f_list) if with_path else f_list
