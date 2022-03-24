height=float(input("Podaj swoj wzrost\n"))
weight=float(input("Podaj swoja wage\n"))
wynik=weight/(height*height)
if wynik<20:
    print("Twoje BMI wynosi:", wynik,".\nI jest to niedowaga")
elif wynik>=20 and wynik<=25:
    print("Twoje BMI wynosi:", wynik,".\nI jest to waga prawidlowa.")
elif wynik>=25 and wynik<=30:
    print("Twoje BMI wynosi:", wynik,".\nI jest to nadwaga.")
else:
    print("Twoje BMI wynosi:", wynik,".\nI jest to otylosc.")
