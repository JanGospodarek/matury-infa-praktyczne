## zadanie 4 - liczby bin

f= open('./Dane_PR/liczby.txt')
lines=f.read().strip().split('\n')

## 1

def zadanie1():
    liczba_liczb=0
    for liczba in lines:
        licza_0=0
        liczba_1=0
        for i in liczba:
            if int(i)==1:
                liczba_1+=1
            if int(i)==0:
                licza_0+=1
        if licza_0>liczba_1:
            liczba_liczb+=1
    return liczba_liczb

# print(zadanie1())

# 2
def bin_to_dec(n):
    k=0
    suma=0
    for i in range(len(n)-1,-1,-1):
        liczba=int(n[i])
        suma+=liczba*2**k
        k+=1
    return suma
def zadanie2():
    podz_2=0
    podz_8=0
    for liczba_bin in lines:
        liczba_dec=bin_to_dec(liczba_bin)
        if liczba_dec%2==0:
            podz_2+=1
        if liczba_dec%8==0:
            podz_8+=1
    return podz_2,podz_8

print(zadanie2())
## 3
def zadanie3():
    min=lines[0]
    max=lines[0]
    min_i=0
    max_i=0
    for i in range(len(lines)):
        liczba_bin=lines[i]
        liczba_dec=bin_to_dec(liczba_bin)
        if liczba_dec<bin_to_dec(min):
            min=liczba_bin
            min_i=i
        if liczba_dec>bin_to_dec(max):
            max=liczba_bin
            max_i=i
    return max_i+1,min_i+1,max,min

print(zadanie3())
