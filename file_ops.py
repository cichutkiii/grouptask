import urllib.request

from pip._vendor.distlib.compat import raw_input

import data_ops
import string
import os

import stat_var


def download_file():

    question = raw_input("czy pobrac plik z internetu?")
    if question == "T" :
        address = raw_input("podaj adres do sciagniecia")
        try:
            print("Sciaganie pliku....")
            urllib.request.urlretrieve(address, stat_var.local_file_name)
            print("Gotowe")
            return stat_var.local_file_name
        except urllib.error.URLError:
            print("nie mozna sciagnac pliku")
    elif question == "N":
        local_file = raw_input("podaj adres nazwe pliku lokalnego")
        if os.path.exists(local_file):
            return local_file
        else:
            print("brak pliku")
            return 0


def write_statistics():
    file = open(stat_var.stat_file, "w+")
    file.write(data_ops.get_count_letter() + "\n")
    file.write("liczba wyrazow: " + str(data_ops.get_count_words()) + "\n")
    file.write("liczba znakow interpunkcyjnych: " + str(data_ops.get_count_punctuation()) + "\n")
    file.write("liczba zdań: " + str(data_ops.get_count_sentences()) + "\n")
    file.close()


def remove_files():
    if os.path.exists(stat_var.stat_file):
        os.remove(stat_var.stat_file)
        print("usunieto plik statystyki")

    else:
        print("plik statystyki nie istnieje")
    if os.path.exists(stat_var.local_file_name):
        os.remove(stat_var.local_file_name)
        print("usunieto plik z danymi")
    else:
        print("plik z danymi nie istnieje")