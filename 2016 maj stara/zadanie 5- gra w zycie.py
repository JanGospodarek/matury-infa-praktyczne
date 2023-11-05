f = open('./Dane/gra.txt')

lines = f.read().split('\n')
komorki = []
for l in lines:
    tab = list(l)
    komorki.append(tab)


# print(komorki)


def komorki_w_pokoleniu(n):
    pokolenia = []
    pokolenia.append(komorki)
    for i in range(n):
        pokolenie = []
        pokolenie_poprzednie = pokolenia[i]
        # print(pokolenie_poprzednie)
        for wiersz in range(len(pokolenie_poprzednie)):
            nowy_wiersz = []
            for index_kom in range(len(pokolenie_poprzednie[wiersz])):
                sasiedzi = []
                # warunek dla komórek na górze i na dole
                index_sasiedniego_wiersza = 1
                if wiersz == 0:
                    index_sasiedniego_wiersza = -1
                if wiersz == 11:
                    index_sasiedniego_wiersza = 0
                if index_sasiedniego_wiersza != 1:
                    sasiedzi.append(pokolenie_poprzednie[index_sasiedniego_wiersza][index_kom])
                    if index_kom - 1 >= 0:
                        sasiedzi.append(pokolenie_poprzednie[index_sasiedniego_wiersza][index_kom - 1])
                    if index_kom + 1 <= 19:
                        sasiedzi.append(pokolenie_poprzednie[index_sasiedniego_wiersza][index_kom + 1])
                # warunek dla komórek na bokach
                index_sasiedniej_kolumny = 1

                if index_kom == 0:
                    index_sasiedniej_kolumny = -1
                if index_kom == 19:
                    index_sasiedniej_kolumny = 0
                if index_sasiedniej_kolumny != 1:
                    sasiedzi.append(pokolenie_poprzednie[wiersz][index_sasiedniej_kolumny])
                    if wiersz - 1 > -1:
                        # print(wiersz)
                        sasiedzi.append(pokolenie_poprzednie[wiersz - 1][index_sasiedniej_kolumny])
                    if wiersz + 1 < 12:
                        sasiedzi.append(pokolenie_poprzednie[wiersz + 1][index_sasiedniej_kolumny])
                for w in range(wiersz - 1, wiersz + 2):
                    if w >= 0 and w <= 11:
                        for w_i in range(len(pokolenie_poprzednie[w])):
                            if w_i + 1 == index_kom or w_i == index_kom or w_i - 1 == index_kom:
                                if not (w_i == index_kom and w == wiersz):
                                    sasiedzi.append(pokolenie_poprzednie[w][w_i])
                # if pokolenie_poprzednie[wiersz][index_kom] == 'X':
                #     print(sasiedzi)
                if pokolenie_poprzednie[wiersz][index_kom] == 'X':
                    if sasiedzi.count('X') == 2 or sasiedzi.count('X') == 3:
                        nowy_wiersz.append('X')
                    else:
                        nowy_wiersz.append('.')
                if pokolenie_poprzednie[wiersz][index_kom] == '.':
                    if sasiedzi.count('X') == 3:
                        nowy_wiersz.append('X')
                    else:
                        nowy_wiersz.append('.')
            pokolenie.append(nowy_wiersz)
        pokolenia.append(pokolenie)
    return pokolenia[-1]


pokolenie_37 = komorki_w_pokoleniu(1)
for l in pokolenie_37:
    print(l)
