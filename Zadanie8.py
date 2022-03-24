import random
zakresa=int(input("Podaj poczatek zakresu do losowania\n"))
zakresb=int(input("Podaj koniec zakresu do losowania\n"))
for i in range(6):
    print(random.randint(zakresa, zakresb))