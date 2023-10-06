## zadanie 6

alfabet=[]
for i in range(65,91):
    alfabet.append(chr(i))

f1=open('./Dane_NOWA/dane_6_1.txt')
f1_wynik=open('./wynik_6_1.txt','wt')
f2_wynik=open('./wynik_6_2.txt','wt')
f2=open('./Dane_NOWA/dane_6_2.txt')
f3=open('./Dane_NOWA/dane_6_3.txt')
lines1=f1.read().strip().split('\n')
lines2=f2.read().strip().split('\n')
lines3=f3.read().strip().split('\n')

## 1
zaszyfrowane=[]
for slowo in lines1:
    szyfr=""
    for i in slowo:
        litera=107+ord(i)
        while litera>ord('Z')+1 or litera<ord('A'):
            if litera > ord('Z'):
                litera -= 26
            elif litera < ord('A'):
                litera += 26
        szyfr+=chr(litera)
    f1_wynik.write(szyfr+'\n')
    zaszyfrowane.append(szyfr)
# print(zaszyfrowane)

## 2
def dekoduj(zaszyfrowane,klucz):
    rozszyfrowane=""
    for i in zaszyfrowane:
        litera=-klucz+ord(i)
        while litera>ord('Z')+1 or litera<ord('A'):
            if litera > ord('Z'):
                litera -= 26
            elif litera < ord('A'):
                litera += 26
        rozszyfrowane+=chr(litera)
    return rozszyfrowane

for line in lines2:
    slowo_zaszyfrowane=line.split(" ")[0]
    if line.split(" ")[1]=="":
        continue
    klucz=int(line.split(" ")[1])
    rozszyfrowane= dekoduj(slowo_zaszyfrowane,klucz)
    f2_wynik.write(rozszyfrowane+'\n')

## 3
zle_zaszyfrowane=[]
for line in lines3:
    slowo = line.split(" ")[0]
    slowo_zaszyfrowane = line.split(" ")[1]
    klucz=abs(ord(slowo[0])-ord(slowo_zaszyfrowane[0]))
    bledne=False
    for i in range(1,len(slowo)):
        nowy_klucz=abs(ord(slowo[i])-ord(slowo_zaszyfrowane[i]))
        if klucz!= nowy_klucz and klucz!=26-nowy_klucz:
            bledne=True
    if bledne:
        zle_zaszyfrowane.append(slowo)
print(zle_zaszyfrowane)