## zadanie 2
import math


## 1.1 czy pierwsza z dokladnoscia sqrt(2)

def czy_pierwsza(n):
    if n<2:
        return False
    for i in range(2,round(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
print(czy_pierwsza(1))

## 1.2
def sumy(n,k):
    suma=0
    while n>0:
        suma+=n%k
        n=n//k
    return suma
for i in range(1,100000):
    suma_bin=sumy(i,2)
    suma_dec=sumy(i,10)
    if czy_pierwsza(i) and czy_pierwsza(suma_bin) and czy_pierwsza(suma_dec):
        print(i)
