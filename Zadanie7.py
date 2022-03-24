import math
dzial=int(input("Wybierz dzialanie:\nJezeli chcesz wybrac dodawanie wprowadz 1\nJezeli chcesz wybrac odejmowanie wprowadz 2\nJezeli chcesz wybrac mnozenie wprowadz 3\nJezeli chcesz wybrac dzielenie wprowadz 4\nJezeli chcesz wybrac potegowanie wprowadz 5\nJezeli chcesz wybrac funkcje hypotenuse wprowadz 6\n"))
if dzial==1:
    print("Wybrane zostalo dodawanie:\n")
    a=int(input("Podaj pierwsza liczbe do dodania\n"))
    b=int(input("Podaj druga liczbe do dodania\n"))
    print("Suma 2 podanych przez ciebie liczb to: ",a+b"\n")
elif dzial==2:
    print("Wybrane zostalo odejmowanie:\n")
    a=int(input("Podaj pierwsza liczbe do odejmowania\n"))
    b=int(input("Podaj liczbe ktora chcesz odjac od pierwszej\n"))
    print("Roznica 2 podanych przez ciebie liczb to: ",a-b"\n")
elif dzial==3:
    print("Wybrane zostalo mnozenie:\n")
    a=int(input("Podaj pierwsza liczbe do pomnozenia\n"))
    b=int(input("Podaj druga liczbe do pomnozenia\n"))
    print("Iloczyn 2 podanych przez ciebie liczb to: ",a*b"\n")
elif dzial==4:
    print("Wybrane zostalo dzielenie:\n")
    a=int(input("Podaj pierwsza do podzielenia\n"))
    b=int(input("Podaj liczbe ktora ma byc dzielnikiem\n"))
    if b==0:
        print("Nie dziel przez 0\n")
    else:
        print("Iloraz 2 podanych przez ciebie liczb to: ",a/b"\n") 
elif dzial==5:
    print("Wybrane zostalo potegowanie:\n")
    a=int(input("Podaj liczbe ktora bedzie podstawa potegi\n"))
    b=int(input("Podaj liczbe ktora bedzie wykladnikiem potegi\n"))
    print("Iloczyn 2 podanych przez ciebie liczb to: ", math.pow(a, b))
elif dzial==6:
    print("Wybrana zostala funkcja hypotenuse:\n")
    a=int(input("Podaj dlugosc pierwszej przyprostokatnej\n"))
    b=int(input("Podaj dlugosc drugiej przyprostokatnej\n"))
    if a<=0 or b<=0:
        print("Podane dlugosci bokow nie sa poprawne")
    else:
      print("Dlugosc przeciwprostokatnej tego trojkata to ", math.hypot(a, b))

