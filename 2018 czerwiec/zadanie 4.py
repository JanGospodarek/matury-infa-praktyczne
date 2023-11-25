f1 = open('./NM_DANE_PR/dane1.txt')
f2 = open('./NM_DANE_PR/dane2.txt')
lines1 = f1.read().strip().split('\n')
lines2 = f2.read().strip().split('\n')
f_lines1 = []
f_lines2 = []
# przygotowanie danych
for line in lines1:
    tab = line.split(" ")
    et = []
    for l in tab:
        et.append(int(l))
    f_lines1.append(et)
for line in lines2:
    tab = line.split(" ")
    et = []
    for l in tab:
        et.append(int(l))
    f_lines2.append(et)

# def zad1():
#     ile = 0
#     for i in range(len(f_lines1)):
#         if f_lines1[i][-1] == f_lines2[i][-1]:
#             ile += 1
#     return ile
#
#
# print(zad1())

# def zad2():
#     ile = 0
#     for i in range(len(f_lines1)):
#         ile_parz1 = 0
#         ile_nparz1 = 0
#         ile_parz2 = 0
#         ile_nparz2 = 0
#         for l in range(len(f_lines1[i])):
#             if f_lines1[i][l] % 2 == 0:
#                 ile_parz1 += 1
#             else:
#                 ile_nparz1 += 1
#         for l in range(len(f_lines2[i])):
#             if f_lines2[i][l] % 2 == 0:
#                 ile_parz2 += 1
#             else:
#                 ile_nparz2 += 1
#         if ile_parz1 == 5 and ile_nparz1 == 5 and ile_parz2 == 5 and ile_nparz2 == 5:
#             ile += 1
#     return ile
#
#
# print(zad2())

# def zad3():
#     ile = 0
#     numery = []
#     for i in range(len(f_lines1)):
#         set1 = set(f_lines1[i])
#         set2 = set(f_lines2[i])
#         czy_podobne = True
#         for l in set1:
#             if l not in set2:
#                 czy_podobne = False
#         for l in set2:
#             if l not in set1:
#                 czy_podobne = False
#         if czy_podobne:
#             ile += 1
#             numery.append(i + 1)
#     return ile, numery
#
#
# print(zad3())
# f_wyn = open('./wynik4_4.txt', 'wt')
#
#
# def zad4():
#     for i in range(len(f_lines1)):
#         ciag1 = f_lines1[i]
#         ciag2 = f_lines2[i]
#         l1 = 0
#         l2 = 0
#         ciag_wyn = []
#         while l1 < len(ciag1) and l2 < len(ciag2):
#             if ciag1[l1] <= ciag2[l2]:
#                 ciag_wyn.append(ciag1[l1])
#                 l1 += 1
#             else:
#                 ciag_wyn.append(ciag2[l2])
#                 l2 += 1
#         reszta = []
#         if l1 == len(ciag1):
#             reszta = ciag2[l2:]
#         else:
#             reszta = ciag1[l1:]
#         for liczba in reszta:
#             ciag_wyn.append(liczba)
#         for liczba in ciag_wyn:
#             f_wyn.write(f'{str(liczba)} ')
#         f_wyn.write('\n')
#
#
# zad4()
