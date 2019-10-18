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


def get_count_sentences():
    with open(stat_var.local_file_name) as dataFile:
        text = dataFile.read()
    return len(text.split("."))


def get_letters_report():
    with open(stat_var.local_file_name) as dataFile:
        text = dataFile.read()
    text_count = Counter(text.translate(str.maketrans('', '', string.punctuation)))
    text_count = {k: text_count.get(k, 0) for k in string.ascii_lowercase}
    for letter in text_count:
        print(letter.upper(), ":", text_count[letter])
