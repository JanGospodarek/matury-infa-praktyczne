f = open('./MIN-R2A1P-163_dane/liczby.txt')
lines = f.read().strip().split('\n')


def zad1():
    ile_8 = 0
    for liczba in lines:
        if liczba[-1] == "8":
            ile_8 += 1
    return ile_8


# print(zad1())
def zad2():
    ile_4 = 0
    for liczba in lines:
        if liczba[-1] == "4" and liczba.count('0') == 0:
            ile_4 += 1
    return ile_4


# print(zad2())

def any_to_dec(bin: str, podstawa: int):
    dec = 0
    k = 0
    for i in range(len(bin) - 1, -1, -1):
        dec += podstawa ** k * int(bin[i])
        k += 1
    return dec


def zad3():
    ile_2 = 0
    for liczba in lines:
        tab = list(liczba)
        podstawa = tab.pop()
        if podstawa == '2' and any_to_dec("".join(tab), 2) % 2 == 0:
            ile_2 += 1
    return ile_2


# print(zad3())
def zad4():
    suma = 0
    for liczba in lines:
        tab = list(liczba)
        podstawa = tab.pop()
        dec = any_to_dec("".join(tab), 8)
        if podstawa == '8':
            suma += dec
    return suma


# print(zad4())

def zad5():
    tab_1 = list(lines[0])
    podstawa_1 = tab_1.pop()
    dec_1 = any_to_dec("".join(tab_1), int(podstawa_1))
    max = [lines[0], dec_1]
    min = [lines[0], dec_1]
    for liczba in lines:
        tab = list(liczba)
        podstawa = tab.pop()
        dec = any_to_dec("".join(tab), int(podstawa))
        if dec > max[1]:
            max[0] = liczba
            max[1] = dec
        if dec < min[1]:
            min[0] = liczba
            min[1] = dec
    return max, min

# print(zad5())
