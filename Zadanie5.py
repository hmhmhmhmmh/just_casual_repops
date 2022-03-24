a=int(input("Podaj dlugosc pierwszego boku trojkata"))
b=int(input("Podaj dlugosc drugiego boku trojkata"))
c=int(input("Podaj dlugosc trzeciego boku trojkata"))
if a+b>c and b+c>a and c+a>b:
    print("Taki trojkat mozna stworzyc.")

else:
    print("Takiego trojkata nie da sie stworzyc.")
