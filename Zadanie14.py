import random

lpopr=[]
lpopr.append(random.sample(range(51), 6))
lstrzel=[]

for i in range(6):
    podana=int(input("Podaj liczbe ktora chcesz strzelic\n"))
    while podana in lstrzel:
        podana=int(input("Podaj inna liczbe \n"))
    else:
        lstrzel.append(podana)
    
lstrzel.sort()
lpopr.sort()

print(f"Podane przez ciebie liczby to: {lstrzel}")

if lpopr==lstrzel:
    print("brawo wygrales w totka :)")
else:
    for element in lstrzel:
        if element in lpopr:
            lstrzel.remove(element)

print(f"Ilosc liczb podanych blednie: {len(lstrzel)}")
print(f"Poprawnymi liczbami były następujące liczby: {lpopr}")
