import math

f = open('./Dane_PR/dane.txt')
lines = f.read().strip().split('\n')


## zadanie 1

def zad1():
    najjasniejszy = int(lines[0].split(' ')[0])
    najciemniejszy = int(lines[0].split(' ')[0])
    for line in lines:
        tab = line.split(' ')
        for piksel in tab:
            if int(piksel) > najjasniejszy:
                najjasniejszy = int(piksel)
            if int(piksel) < najciemniejszy:
                najciemniejszy = int(piksel)
    return najjasniejszy, najciemniejszy


# print(zad1())

## zadanie 2

def zad2():
    ile_usunac = 0
    for line in lines:
        tab = line.split(' ')
        czy_usunac = False
        for i in range(math.ceil(len(tab) / 2)):
            if tab[i] != tab[len(tab) - 1 - i]:
                czy_usunac = True
        if czy_usunac:
            ile_usunac += 1
    return ile_usunac


# print(zad2())
for i in range(len(lines)):
    lines[i] = lines[i].split(' ')


def is_contrast(n1: str, n2: str):
    if math.fabs((int(n1)) - int(n2)) > 128:
        return True
    return False


def zad3():
    ile_sasiednich = 0

    for i in range(len(lines)):
        for l in range(len(lines[i])):
            # Warunki na sprawdzenie w wierszach
            ile_sasiednich_jeden_px = 0
            if l == 0:
                if is_contrast(lines[i][l], lines[i][l + 1]):
                    ile_sasiednich_jeden_px += 1
            elif l == 319:
                if is_contrast(lines[i][l], lines[i][l - 1]):
                    ile_sasiednich_jeden_px += 1
            else:
                if is_contrast(lines[i][l], lines[i][l + 1]) or is_contrast(lines[i][l], lines[i][l - 1]):
                    ile_sasiednich_jeden_px += 1
            # Warunki na sprawdzenie w kolumnach
            if i == 0:
                if is_contrast(lines[i][l], lines[i + 1][l]):
                    ile_sasiednich_jeden_px += 1
            elif i == 199:
                if is_contrast(lines[i][l], lines[i - 1][l]):
                    ile_sasiednich_jeden_px += 1
            else:
                if is_contrast(lines[i][l], lines[i - 1][l]) or is_contrast(lines[i][l], lines[i + 1][l]):
                    ile_sasiednich_jeden_px += 1
            if ile_sasiednich_jeden_px >= 1:
                ile_sasiednich += 1
    return ile_sasiednich


# print(zad3())

def zad4():
    max_col = 1
    for row_i in range(len(lines[0])):
        dlugosc_linii = 1
        for col_i in range(1, len(lines)):
            if lines[col_i][row_i] == lines[col_i - 1][row_i]:
                dlugosc_linii += 1
                if dlugosc_linii > max_col:
                    max_col = dlugosc_linii
            else:
                dlugosc_linii = 1

    return max_col

# print(zad4())
