import urllib.request

import stat_var


def downloadFile():
    try:
        print("Downloading data....")
        urllib.request.urlretrieve(stat_var.fileAddress, stat_var.local_file_name)
        print("Done")
    except urllib.error.URLError:
        print("Couldn't download file, check connection")
