### zadanie 4
import math

f=open('./Dane_NOWA/punkty.txt')
lines=f.read().strip().split('\n')

def zadanie1():
    punkty_na_okregu=[]
    punkty_we_wnetrzu=0
    for line in lines:
        punkty=line.split(" ")
        x=int(punkty[0])
        y=int(punkty[1])
        rownanie=(x-200)**2+(y-200)**2
        if rownanie==40000:
            punkty_na_okregu.append(line)
        if rownanie<40000:
            punkty_we_wnetrzu+=1

    return [punkty_na_okregu,punkty_we_wnetrzu]


print(zadanie1())

def zadanie2(liczba_punktow):
    srednie_pi=0
    nk=0
    n=10000
    P=160000
    r=200
    for i in range(liczba_punktow):
        punkty=lines[i].split(" ")
        x = int(punkty[0])
        y = int(punkty[1])
        rownanie=((x-200)**2)+((y-200)**2)
        if rownanie<=40000:
            nk+=1
    print(nk,P,n,r)
    srednie_pi=(nk*P)/(n*40000)
    return round(srednie_pi,4)
print(zadanie2(1000),zadanie2(5000),zadanie2(10000))