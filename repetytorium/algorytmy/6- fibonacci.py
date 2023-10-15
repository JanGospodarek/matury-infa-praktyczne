## zadanie 6 fibonacci

def czy_w_fib(x):
    wartosc_wyrazu_1=1
    wartosc_wyrazu_2=1
    while wartosc_wyrazu_2<=x:
        suma=wartosc_wyrazu_1+wartosc_wyrazu_2
        wartosc_wyrazu_1=wartosc_wyrazu_2
        wartosc_wyrazu_2=suma
        if wartosc_wyrazu_2==x:
            return  True
    return False
## 6.2 szyfrowanie
def szyfrowanie(tekst:str,n:int):
    tekst=tekst.replace(" ","")
    klucz=[1]*len(tekst)
    zaszyfrowane=[]
    for i in range(2,len(tekst)):
        klucz[i]=(klucz[i-1]+klucz[i-2]) %n
    for i in range(len(tekst)):
        kod=ord(tekst[i])+klucz[i]
        while kod>ord('Z'):
            kod-=26
        nowy=chr(kod)
        zaszyfrowane.append(nowy)
    print(zaszyfrowane)
print(szyfrowanie('DOSTAWA W CZWARTEK',20))
