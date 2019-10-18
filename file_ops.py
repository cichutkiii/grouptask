import urllib.request
import data_ops
import string
import os

import stat_var


def download_file():
    try:
        print("Sciaganie pliku....")
        urllib.request.urlretrieve(stat_var.fileAddress, stat_var.local_file_name)
        print("Gotowe")
    except urllib.error.URLError:
        print("nie mozna sciagnac pliku, sprawdz polaczenie")


def write_statistics():
    file = open(stat_var.stat_file, "w+")
    file.write("liczba liter: " + str(data_ops.get_count_sentences()) + "\n")
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