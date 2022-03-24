import random

liczby=[]
wylosowana=(random.randint(1, 20))
podana=int(input("Podaj liczbe ktora myslisz ze zostala wylosowana\n"))
liczby.append(podana)

if podana==wylosowana:
    print("Brawo zgadles liczbe za pierwszym razem!")
else:
    while podana!=wylosowana:
        podana=int(input("Sprobuj ponownie\n"))
        liczby.append(podana)
    else:
        print(f"Odgadniecie liczby zajelo ci {len(liczby)} prob.")

