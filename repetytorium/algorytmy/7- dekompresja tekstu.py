## zadanie 7- dekompresja tekstu

def dekompresja(tekst:str):
    zdekompresowany=[]
    for i in range(len(tekst)-1,-1,-1):
        if tekst[i].isdigit():
            t=tekst[i-1]*(int(tekst[i])-1)
            zdekompresowany.append(t)
        else:
            zdekompresowany.append(tekst[i])

    return "".join(zdekompresowany[::-1])
print(dekompresja('X3DAZ9KAP2'))
