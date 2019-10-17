import file_ops
import stat_var
import data_ops

pick = 0
file_ops.downloadFile()

while True:
    print(stat_var.menuOptions)
    try:
        pick = int(input(stat_var.yourChoice))
    except ValueError:
        print("Podana wartość nie jest liczbą")

    if pick == 1:
        file_ops.downloadFile()
        # 1. Pobierz plik z internetu
    elif pick == 2:
        if data_ops.check_file_exist():
            count_letters = data_ops.get_count_letter()
            print("liczba liter: ", count_letters)
        else:
            print("brak danych do sprawdzenia")
        # 2. Zlicz liczbę liter w pobranym pliku
    elif pick == 3:
        pass
        # 3. Zlicz liczbę wyrazów w pliku
    elif pick == 4:
        pass
        # 4. Zlicz liczbę znaków interpunkcyjnych w pliku.
    elif pick == 5:
        pass
        # 5. Zlicz liczbę zdań w pliku
    elif pick == 6:
        pass
        # 6. Wygeneruj raport o użyciu liter (A-Z)
    elif pick == 7:
        pass
        # 7. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt
    elif pick == 8:

        # 8. Wyjście z programu
        break
    else:
        print(stat_var.withoutChoice)
