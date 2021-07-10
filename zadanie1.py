obecnyRok = 2021
dataUr = int(input("Wpisz rok urodzenia"))

if dataUr > obecnyRok:
    print("Nieprawidłowy rok urodzenia");
else:
    wiek = obecnyRok - dataUr;
    if wiek >= 18:
        print("Masz", wiek, "lat i jesteś pełnoletni.")
    else:
        print("Masz", wiek, "lat i nie jesteś pełnoletni.")
