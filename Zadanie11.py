wspa=float(input("Podaj pierwsza wpolrzedna swojego punktu\n"))
wspb=float(input("Podaj druga wpolrzedna swojego punktu\n"))
if wspb==0 and wspa!=0:
    print("Ten punkt lezy na osi x")
elif wspa==0 and wspb!=0:
    print("Ten punkt lezy na osi y")
elif wspa==0 and wspb==0:
    print("Ten punkt lezy w punkcie 0 0 ukladu.")
elif wspa>0 and wspb>0:
    print("Ten punkt lezy w cwiartce nr 1")
elif wspa<0 and wspb>0:
    print("Ten punkt lezy w cwiartce nr 2")
elif wspa<0 and wspb<0:
    print("Ten punkt lezy w cwiartce nr 3")
else:
    print("Ten punkt lezy w cwiartce nr 4")