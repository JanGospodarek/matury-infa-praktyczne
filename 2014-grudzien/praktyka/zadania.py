## zadanie 5

f=open("./NAPIS.TXT")
lines=f.read().strip().split('\n')

## zadanie a

def czy_pierwsza(n):
    if n==1:
        return False
    for i in range(2,round(n/2)):
        if n%i==0:
            return False
    return True


def A():
    ile_napisow_pierwszych=0
    for slowo in lines:
        suma_ascii=0
        for litera in slowo:
            wartosc_ascii=ord(litera)
            suma_ascii+=wartosc_ascii
        if czy_pierwsza(suma_ascii):
            ile_napisow_pierwszych+=1

    return ile_napisow_pierwszych

print(f'zadanie a: {A()}')

## zadanie b
def B():
    napisy_rosnace=[]
    for slowo in lines:
        czy_rosnace=True
        for i in range(1,len(slowo)):
            if slowo[i-1]>=slowo[i] and czy_rosnace:
                czy_rosnace=False
        if czy_rosnace:
            napisy_rosnace.append(slowo)
    return napisy_rosnace

print(f'zadanie b: {B()}')

## zadanie c

def C():
   napisy_powtarzajace=[]
   napisy={}
   for slowo in lines:
       if slowo in napisy:
            napisy[slowo]+=1
       else:
           napisy[slowo]=1
   for napis in napisy:
       if napisy[napis]>1:
           napisy_powtarzajace.append(napis)
   return napisy_powtarzajace

print(f'zadanie b: {C()}')