f = open('./Dane_PR/sygnaly.txt')
lines = f.read().strip().split('\n')
import math


# def zad1():
#     wiadomosc = ""
#     for i in range(39, len(lines), 40):
#         wiadomosc += lines[i][9]
#     return wiadomosc
#
#
# print(zad1())

# def zad2():
#     najdl_slowo = lines[0]
#     dlugosc = len(set(list(lines[0])))
#     for slowo in lines:
#         dl = len(set(list(slowo)))
#         if dl > dlugosc:
#             najdl_slowo = slowo
#             dlugosc = dl
#     return najdl_slowo, dlugosc
#
#
# print(zad2())
def zad3():
    for slowo in lines:
        wypisac = True
        base_odl = math.fabs(ord(slowo[0]) - ord(slowo[0]))
        for i in range(len(slowo)):
            for l in range(i, len(slowo)):
                if math.fabs(ord(slowo[i]) - ord(slowo[l])) > 10:
                    wypisac = False
        if wypisac:
            print(slowo)


zad3()
