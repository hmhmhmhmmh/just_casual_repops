dzial=int(input("Wybierz dzialanie:\nJezeli chcesz wybrac dodawanie wprowadz 1\nJezeli chcesz wybrac odejmowanie wprowadz 2\nJezeli chcesz wybrac mnozenie wprowadz 3\nJezeli chcesz wybrac dzielenie wprowadz 4\n"))
if dzial==1:
    print("Wybrane zostalo dodawanie:\n")
    a=int(input("Podaj pierwsza liczbe do dodania"))
    b=int(input("Podaj druga liczbe do dodania"))
    print("Suma 2 podanych przez ciebie liczb to: ",a+b)
elif dzial==2:
    print("Wybrane zostalo odejmowanie:\n")
    a=int(input("Podaj pierwsza liczbe do odejmowania"))
    b=int(input("Podaj liczbe ktora chcesz odjac od pierwszej"))
    print("Roznica 2 podanych przez ciebie liczb to: ",a-b)
elif dzial==3:
    print("Wybrane zostalo mnozenie:\n")
    a=int(input("Podaj pierwsza liczbe do pomnozenia"))
    b=int(input("Podaj druga liczbe do pomnozenia"))
    print("Iloczyn 2 podanych przez ciebie liczb to: ",a*b)
elif dzial==4:
    print("Wybrane zostalo dzielenie:\n")
    a=int(input("Podaj pierwsza do podzielenia"))
    b=int(input("Podaj liczbe ktora ma byc dzielnikiem"))
    if b==0:
        print("Nie dziel przez 0 ty glupia *******")
    else:
        print("Iloraz 2 podanych przez ciebie liczb to: ",a/b)