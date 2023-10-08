## zadanie 1

## 1.1 scalenie dwoch tablich posortowanych

ciag_1=[1,3,5,7,9,12]
ciag_2=[2,6,10,11,12]
n1=len(ciag_1)
n2=len(ciag_2)
ciag_wynikowy=[]
for i in range(n1):
    ciag_wynikowy.append(ciag_1[i])
for i in range(n2):
    ciag_wynikowy.append(ciag_2[i])
## sortowanie babelkowe
for j in range(len(ciag_wynikowy)):
    for i in range(1,len(ciag_wynikowy)-j):
        if ciag_wynikowy[i]<ciag_wynikowy[i-1]:
            temp=ciag_wynikowy[i]
            ciag_wynikowy[i]=ciag_wynikowy[i-1]
            ciag_wynikowy[i-1]=temp
print(ciag_wynikowy)

## 1.2 scalenie tylko unikatów

ciag_1=[2,3,5,7,7,9,12]
ciag_2=[2,6,5,11,12,7]
n1=len(ciag_1)
n2=len(ciag_2)
ciag_wynikowy=[]

for i in range(n1):
    if ciag_1[i] not in ciag_wynikowy:
        ciag_wynikowy.append(ciag_1[i])

for i in range(n2):
    if ciag_2[i] not in ciag_wynikowy:
        ciag_wynikowy.append(ciag_2[i])

print(ciag_wynikowy)

