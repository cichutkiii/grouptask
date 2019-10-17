import os.path
import stat_var
import string
from collections import Counter


def check_file_exist():
    if os.path.exists(stat_var.local_file_name):
        return True
    else:
        return False


def get_count_letter():
    counter = 0
    with open(stat_var.local_file_name) as dataFile:
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        text = dataFile.read()
        for char in text:
            if char in letters:
                counter = counter + 1
    return counter
