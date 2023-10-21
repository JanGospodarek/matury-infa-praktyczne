## zadanie 6 kody kreskowe
f=open('./dane/kody.txt')
lines=f.read().strip().split('\n')
f=open('./dane/cyfra_kodkreskowy.txt')
cyfry_kody=f.read().strip().split('\n')
f_kody1=open('kody1.txt','wt')
f_kody2=open('kody2.txt','wt')
f_kody3=open('kody3.txt','wt')
for i in range(len(cyfry_kody)):
    cyfry_kody[i]=cyfry_kody[i].split("\t")
cyfry_kody.pop(0)

print('abc'[::-1])
def zadanie1():
    for liczba in lines:
        suma_parz=0
        suma_nparz=0
        liczba_rev=liczba[::-1]
        for i in range(len(liczba_rev)):
            if i%2==0:
                suma_parz+=int(liczba_rev[i])
            else:
                suma_nparz+=int(liczba_rev[i])
        print(suma_parz,suma_nparz)
        f_kody1.write(f'{str(suma_parz)} {str(suma_nparz)}\n')

zadanie1()

def zadanie2():
    for liczba in lines:
        suma_parz=0
        suma_nparz=0
        liczba_rev=liczba[::-1]
        for i in range(len(liczba_rev)):
            if i%2==0:
                suma_parz+=int(liczba_rev[i])
            else:
                suma_nparz+=int(liczba_rev[i])

        suma=suma_parz*3+suma_nparz
        reszta=suma%10
        cyfra_kontrolna=str((10-reszta)%10)
        kod_kontrolny=""
        for cyfra in cyfry_kody:
            if cyfra[0]==cyfra_kontrolna:
                kod_kontrolny=cyfra[1]
        print(f'{str(cyfra_kontrolna)} {str(kod_kontrolny)}')
        f_kody2.write(f'{str(cyfra_kontrolna)} {str(kod_kontrolny)}\n')


zadanie2()

def zadanie3():
    for liczba in lines:
        suma_parz=0
        suma_nparz=0
        liczba_rev=liczba[::-1]
        for i in range(len(liczba_rev)):
            if i%2==0:
                suma_parz+=int(liczba_rev[i])
            else:
                suma_nparz+=int(liczba_rev[i])

        suma=suma_parz*3+suma_nparz
        reszta=suma%10
        cyfra_kontrolna=str((10-reszta)%10)
        kod_kontrolny=""
        for cyfra in cyfry_kody:
            if cyfra[0]==cyfra_kontrolna:
                kod_kontrolny=cyfra[1]
        kod_liczby="11011010"
        for i in liczba:
            for cyfra in cyfry_kody:
                if cyfra[0]==str(i):
                    kod_liczby+=cyfra[1]
        kod_liczby+=kod_kontrolny+"11010110"
        f_kody3.write(f'{kod_liczby}\n')


zadanie3()

