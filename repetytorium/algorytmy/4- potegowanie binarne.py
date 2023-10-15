## zadanie 4.2- potegowanie binarne

def oblicz(x,n):
    w=1
    if n==0:
        return 1
    if n==1:
        return x
    for i in range(n):
        w=w*x
    return w
print(oblicz(2,10))