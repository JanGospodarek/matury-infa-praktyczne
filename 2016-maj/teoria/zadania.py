## 1.2

a=75
def suma(n):
    dzielniki = []

    for i in range(1,int(n/2+1)):
        if n%i==0:
            dzielniki.append(i)
    liczba_skojarzona=0
    for i in dzielniki:
        liczba_skojarzona+=i
    return liczba_skojarzona
x=suma(a) #suma dzielników a
y=suma(x-1) #suma dzielników b
print(x,y)
if y-1==a:
    print(x-1)
else:
    print("NIE")