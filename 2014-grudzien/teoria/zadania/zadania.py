## 1.2

def znaczace(k):
    i=0
    tab_cyfr=[]
    while k!=0:
        tab_cyfr.append(k%10)
        k=k//10
        i+=1
    print(tab_cyfr,i)


znaczace(54321)

## 1.3

def dupa(k,n,tab_cyfr):
    i=0

    while (i<n):
        k=k-tab_cyfr[i]**n
        i+=1
    print(k)
    if k==0:
        return True
    else:
        return False




print(dupa(153,3,[1,3,5]))

## 3.2

def jajco(s):
    znaki=[]
    ile=0
    for litera in s:
        if not litera in znaki:
            znaki.append(litera)
            ile+=1

    return ile

print(jajco("HANIA"))

