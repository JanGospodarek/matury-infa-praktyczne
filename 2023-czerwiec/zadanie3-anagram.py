## Anagram binarny

##czas- 58 minut

plik_przyklad=open('./DANE/DANE_E/anagram.txt')
plik_odpowiedzi=open('./wyniki3.txt','wt')
lines = plik_przyklad.read().strip().split('\n')
## zadanie 1
## czas- 5:40
def zadanie_1():
    liczba_zrownowazonych=0
    liczba_prawie_zrownozanoych=0
    for liczba in lines:
        liczba_0=liczba.count("0")
        liczba_1=liczba.count("1")
        if liczba_0==liczba_1:
            liczba_zrownowazonych+=1
        elif liczba_0+1==liczba_1:
            liczba_prawie_zrownozanoych+=1
        elif liczba_1+1==liczba_0:
            liczba_prawie_zrownozanoych+=1
    return [liczba_zrownowazonych,liczba_prawie_zrownozanoych]
plik_odpowiedzi.write(f'zadanie 3.1: {zadanie_1()} \n')
print(zadanie_1())

## zadanie 2

import itertools
def zadanie_2():
    anagrams={}
    for liczba in lines:
        if not len(liczba)==8:
            continue
        tab=list(liczba)[1:]
        permutations=list(set(itertools.permutations(tab)))
        anagrams[liczba]=len(permutations)
    sorted_anagrams=sorted(anagrams.items(),key=lambda x:x[1], reverse=True)
    filtered=[]
    for i in range(len(sorted_anagrams)):
        if sorted_anagrams[i][1]==sorted_anagrams[0][1]:
            filtered.append(sorted_anagrams[i][0])
    return filtered
wynik=zadanie_2()
plik_odpowiedzi.write("zadanie 3.2: \n")
for liczba in wynik:
    plik_odpowiedzi.write(f' {liczba} \n')

print(zadanie_2())

## zadnaie 3
import math

def bin_to_decimal(binary_num):
    potega=len(binary_num)-1
    dec=0
    for num in binary_num:
        dec+=2**potega*int(num)
        potega-=1
    return dec

def dec_to_bin(decimal_num):
    reszty=[]
    while decimal_num>0:
        reszty.append(str(decimal_num%2))
        decimal_num=decimal_num//2
    return "".join(reszty[::-1])

def zadanie_3():
    max_roznica=math.fabs(bin_to_decimal(lines[1])-bin_to_decimal(lines[0]))
    for i in range(1,len(lines)):
        roznica=math.fabs(bin_to_decimal(lines[i])-bin_to_decimal(lines[i-1]))
        if roznica>max_roznica:
            max_roznica=roznica
    return dec_to_bin(int(max_roznica))
print(zadanie_3())
plik_odpowiedzi.write(f'zadanie 3.3: {zadanie_3()} \n')
## zadanie 4

def zadanie_4():
    ile_bez_0=0
    ## A
    for bin_num in lines:
        dec_str=str(bin_to_decimal(bin_num))
        ile_0=dec_str.count("0")
        if ile_0==0:
            ile_bez_0+=1
    ## B
    liczba_najwieksza_suma_cyfr=str(bin_to_decimal(lines[0]))
    najwieksza_suma_cyfr=0
    for letter in set(list(str(bin_to_decimal(lines[0])))):
        najwieksza_suma_cyfr+=int(letter)

    for bin_num in lines:
        dec_str=str(bin_to_decimal(bin_num))
        suma_cyfr=0
        for letter in set(list(dec_str)):
            suma_cyfr += int(letter)
        if suma_cyfr>najwieksza_suma_cyfr:
            najwieksza_suma_cyfr=suma_cyfr
            liczba_najwieksza_suma_cyfr=int(dec_str)
    return [ile_bez_0,liczba_najwieksza_suma_cyfr]

print(zadanie_4())
wynik4=zadanie_4()
plik_odpowiedzi.write("zadanie 3.4:")
for liczba in wynik4:
    plik_odpowiedzi.write(f' {liczba} ')
