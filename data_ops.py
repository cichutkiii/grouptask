import os.path
import stat_var
import string


def check_file_exist():
    if os.path.exists(stat_var.local_file_name):
        return True
    else:
        return False


def get_count_letter():
    counter = 0
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open(stat_var.local_file_name) as dataFile:
        text = dataFile.read()
        for char in text:
            if char in letters:
                counter = counter + 1
    return counter


def get_count_words():
    with open(stat_var.local_file_name) as dataFile:
        text = dataFile.read()
    return len(text.split())


def get_count_punctuation():
    counter = 0
    with open(stat_var.local_file_name) as dataFile:
        text = dataFile.read()
        for char in text:
            if char in string.punctuation:
                counter = counter + 1
    return counter
