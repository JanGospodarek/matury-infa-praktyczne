f = open('../dane/rozdział 2/pliki/20/anagramy.txt')
lines = f.read().strip().split('\n')


def czy_palindrom(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1) // 2 + 1):
        if str1[i] != str2[len(str2) - 1 - i]:
            return False
    return True


def czy_anagram(str1, str2):
    ile_l2 = {}

    ile_l1 = {}
    for litera in str1:
        if litera in ile_l1.keys():
            ile_l1[litera] += 1
        else:
            ile_l1[litera] = 1
    for litera in str2:
        if litera in ile_l2.keys():
            ile_l2[litera] += 1
        else:
            ile_l2[litera] = 1
    for key in ile_l1.keys():
        if key not in ile_l2.keys():
            return False
        if ile_l2[key] != ile_l1[key]:
            return False
    for key in ile_l2.keys():
        if key not in ile_l1.keys():
            return False
        if ile_l2[key] != ile_l1[key]:
            return False
    return True


def zad1():
    ile = 0
    for line in lines:
        str1 = line.split(' ')[0]
        str2 = line.split(' ')[1]
        if czy_anagram(str1, str2):
            ile += 1
    print(ile)


zad1()


def zad2():
    for line in lines:
        str1 = line.split(' ')[0]
        str2 = line.split(' ')[1]
        if not czy_anagram(str1, str2) and len(str1) == len(str2):
            ile_l1 = {}
            ile_l2 = {}
            for litera in str1:
                if litera in ile_l1.keys():
                    ile_l1[litera] += 1
                else:
                    ile_l1[litera] = 1
            for litera in str2:
                if litera in ile_l2.keys():
                    ile_l2[litera] += 1
                else:
                    ile_l2[litera] = 1
            do_zmiany1 = ''
            do_zmiany2 = ''
            for key in ile_l2.keys():
                if key not in ile_l1.keys():
                    if ile_l2[key] == 1:
                        do_zmiany2 = key
                        break
                elif ile_l1[key] == ile_l2[key] - 1:
                    do_zmiany2 = key
                    break
            for key in ile_l1.keys():
                if key not in ile_l2.keys():
                    if ile_l1[key] == 1:
                        do_zmiany1 = key
                        break
                elif ile_l2[key] == ile_l1[key] - 1:
                    do_zmiany1 = key
                    break
            if do_zmiany2 != '' and do_zmiany1 != '':
                index = -1
                for i, litera in enumerate(str2):
                    if litera == do_zmiany2 and index == -1:
                        index = i
                index += 1
                print(str1, str2, do_zmiany1, index, 'zamiana z :', do_zmiany2)


# zad2()

def kombinacje(slowo):
    slowa = []

    def generuj(prefiks, pozostale):
        print(prefiks, pozostale)
        if len(pozostale) == 0:
            slowa.append(prefiks)
            return
        for i in range(len(pozostale)):
            generuj(prefiks + pozostale[i], pozostale[:i] + pozostale[i + 1:])

    generuj("", slowo)
    return list(set(slowa))


def zad3():
    print(kombinacje('bura'))


zad3()


def zad4():
    f_w = open('../dane/rozdział 2/pliki/20/wyrazy.txt')
    l_w = f_w.read().strip().split('\n')
    for line in l_w:
        print(kombinacje(line))

# zad4()
