import random

pktprog=[]
pktczl=[]

while len(pktczl)!=3 and len(pktprog)!=3:
    wybor=(input("\nWybierz Papier Kamien lub Nozyce\n"))

    papier=["papier", "Papier" ]
    kamien=["Kamien", "kamien", "kamień", "Kamień"]
    nozyce=["nozyce", "Nozyce"]

    wylosowana=(random.randint(1,3))
    if wylosowana==1:
        wylosowana="papier"
        wylosowanab="Papier"
        wylosowanac="papier"
        wylosowanad="papier"
    elif wylosowana==2:
        wylosowana="kamien"
        wylosowanab="Kamien"
        wylosowanac="Kamień"
        wylosowanad="kamień"
    else:
        wylosowana="nozyce"
        wylosowanab="Nozyce"
        wylosowanac="Nozyce"
        wylosowanad="Nozyce"

    if wybor==wylosowana or wybor==wylosowanab or wybor==wylosowanac or wybor==wylosowanad:
        print("\nRemis! Wyrzuciliscie to samo")
    #WYBOR PAPIERU
    elif wybor in papier and wylosowana in kamien:
        print("\nWygrales! Komputer wybral kamien")
        pktczl.append(1)
    elif wybor in papier and wylosowana in nozyce:
        print("\nPrzegrales! Komputer wybral nozyce")
        pktprog.append(1)
    #WOBOR KAMIENIA
    elif wybor in kamien and wylosowana in papier:
        print("\nPrzegrales! Komputer wybral papier")
        pktprog.append(1)
    elif wybor in kamien and wylosowana in nozyce:
        print("\nWygrales! Komputer wybral nozyce")
        pktczl.append(1)
    #WYBOR NOZYC
    elif wybor in nozyce and wylosowana in kamien:
        print("\nPrzegrales! Komputer wybral kamien")
        pktprog.append(1)
    else:
        print("\nWygrales! Komputer wybral papier")
        pktczl.append(1)
else:
    if len(pktczl)==3:
        print("\nOsiagnales 3 punkty - wygrales!")
    else:
        print("\nKomputer osiagnal 3 punkty wiec przegrywasz")
