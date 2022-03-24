from math import sqrt


def maks2liczb (a, b):
  if a>b:
    return a
  else:
      return b

def min3liczb (a, b, c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    elif c<a and c<b:
        return c

def parzystoscliczby (a):
    if a%2==0:
        return "Ta liczba jest parzysta"
    else:
        return "Ta liczba jest nieparzysta"

def wartoscbezwzgl (a):
    a=a*a
    a=sqrt(a)
    return a

def sumawielu (*args):
    