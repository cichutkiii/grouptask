import urllib.request
import data_ops
import string

import stat_var


def downloadFile():
    try:
        print("Downloading data....")
        urllib.request.urlretrieve(stat_var.fileAddress, stat_var.local_file_name)
        print("Done")
    except urllib.error.URLError:
        print("Couldn't download file, check connection")


def write_statistics():
    file = open(stat_var.stat_file, "w+")
    file.write("liczba liter: " + str(data_ops.get_count_sentences()) + "\n")
    file.write("liczba wyrazow: " + str(data_ops.get_count_words()) + "\n")
    file.write("liczba znakow interpunkcyjnych: " + str(data_ops.get_count_punctuation()) + "\n")
    file.write("liczba zdań: " + str(data_ops.get_count_sentences()) + "\n")
    file.close()
