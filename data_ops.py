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
    counteraei = 0
    counterbcd = 0
    lettersaeiou = "aeiouyAEIOUY"
    lettersbcd = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    with open(stat_var.local_file_name) as dataFile:
        text = dataFile.read()
        for char in text:
            if char in lettersaeiou:
                counteraei = counteraei + 1
        for char in text:
            if char in lettersbcd:
                counterbcd = counterbcd + 1
    print("liczba samoglosek", counteraei)
    print("liczba spolglosek", counterbcd)
    result = "liczba samoglosek: " + str(counteraei) + "\nliczba spolglosek: " + str(counterbcd)
    return result


def get_count_words():
    counter = 0
    with open(stat_var.local_file_name) as dataFile:
        text = dataFile.read()
        words = text.split()
        for word in words:
            if len(word) > 1:
                counter = counter + 1
    return counter


def get_count_punctuation():
    counter = 0
    with open(stat_var.local_file_name) as dataFile:
        text = dataFile.read()
        for char in text:
            if char in ".?":
                counter = counter + 1
    return counter


def get_count_sentences():
    with open(stat_var.local_file_name) as dataFile:
        text = dataFile.read()
        zdania = (str(len(text.split("."))) + str(len(text.split("?"))))
    return zdania


def get_letters_report():
    with open(stat_var.local_file_name) as dataFile:
        text = dataFile.read()
    text_count = Counter(text.translate(str.maketrans('', '', string.punctuation)))
    text_count = {k: text_count.get(k, 0) for k in string.ascii_lowercase}
    for letter in text_count:
        print(letter.upper(), ":", text_count[letter])
    return text_count
