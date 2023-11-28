import math

f = open('./dane4.txt')
lines = f.read().strip().split('\n')


def zad1():
    max = 0
    min = math.fabs(int(lines[0]) - int(lines[1]))
    for i in range(1, len(lines)):
        luka = int(math.fabs(int(lines[i - 1]) - int(lines[i])))
        if luka > max:
            max = luka
        if luka < min:
            min = luka
    return max, min


# print(zad1())

def zad2():
    max_fragment = []
    max_dl = 2

    akt_fragment = [lines[0], lines[1]]
    akt_dl = 2
    akt_luka = int(math.fabs(int(lines[0]) - int(lines[1])))
    for i in range(2, len(lines)):
        luka = int(math.fabs(int(lines[i - 1]) - int(lines[i])))
        if luka == akt_luka:
            akt_dl += 1
            akt_fragment.append(lines[i])
        else:
            if akt_dl > max_dl:
                max_dl = akt_dl
                max_fragment = akt_fragment
            akt_dl = 2
            akt_fragment = [lines[i - 1], lines[i]]
            akt_luka = luka
    return max_dl, max_fragment[0], max_fragment[-1]


# print(zad2())
def zad3():
    luki = {}
    for i in range(1, len(lines)):
        luka = int(math.fabs(int(lines[i - 1]) - int(lines[i])))
        if luka in luki.keys():
            luki[luka] += 1
        else:
            luki[luka] = 1
    s_luki = sorted(luki.items(), key=lambda x: x[1], reverse=True)
    krotnosc = s_luki[0][1]
    wartosci_luk = []
    for t in s_luki:
        if t[1] == krotnosc:
            wartosci_luk.append(t[0])
    return krotnosc, wartosci_luk


print(zad3())
