f = open('./dane/slowa.txt')

lines = f.read().strip().split('\n')
## zadanie 1
ile_slow = 0
for slowo in lines:
    liczba_0 = 0
    liczba_1 = 0
    for l in slowo:
        if l == '1':
            liczba_1 += 1
        else:
            liczba_0 += 1
    if liczba_0 > liczba_1:
        ile_slow += 1
print(ile_slow)

# zadanie 2
ile_slow_bloki = 0
for slowo in lines:
    # blok_pierwszy=[]
    # blok_drugi=[]
    czy_ok = True
    for i in range(len(slowo)):
        if slowo.count('1') == 0 or slowo.count('0') == 0:
            czy_ok = False
        if slowo[i] != '0':
            pozostaly_blok = slowo[i:]
            if pozostaly_blok.count('0') > 0:
                czy_ok = False
    if czy_ok:
        ile_slow_bloki += 1
print(ile_slow_bloki)
# zadanie 3
bloki_dict = {}
for i in range(len(lines)):
    slowo = lines[i]
    dlugosc_max = 1
    dlugosc_bloku = 1
    for l in range(1, len(slowo)):
        if slowo[l] == slowo[l - 1] and slowo[l - 1] != "1":
            dlugosc_bloku += 1
            if dlugosc_bloku > dlugosc_max:
                dlugosc_max = dlugosc_bloku
        else:
            dlugosc_bloku = 1
    bloki_dict[str(i)] = dlugosc_max
max_dlugosc = bloki_dict['0']
for key in bloki_dict.keys():
    if bloki_dict[key] > max_dlugosc:
        max_dlugosc = bloki_dict[key]
for key in bloki_dict.keys():
    if bloki_dict[key] == max_dlugosc:
        print(lines[int(key)])
print(max_dlugosc)
# print(bloki_dict)
