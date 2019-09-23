import stat_var

pick = 0
while True:
    print(stat_var.menuOptions)
    try:
        pick = int(input(stat_var.yourChoice))
    except ValueError:
        print("Podana wartość nie jest liczbą")

    if pick == 1:
        pass
        # 1. Pobierz plik z internetu
    elif pick == 2:
        pass
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
