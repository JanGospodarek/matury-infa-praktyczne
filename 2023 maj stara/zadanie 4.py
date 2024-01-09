f = open('./Dane_2305/slowa.txt')
lines = f.read().strip().split('\n')


def zad1():
    f_wyn = open('./wyniki4_1.txt', 'wt', encoding='UTF-8')
    for slowo in lines:
        if slowo.count('k') == slowo.count('w'):
            f_wyn.write(f'{slowo} \n')
            print(slowo)
    f_wyn.close()


# zad1()


def zad2():
    f_wyn2 = open('./wyniki4_2.txt', 'wt', encoding='UTF-8')

    wakacje = {
        'w': 1,
        'a': 2,
        'k': 1,
        'c': 1,
        'j': 1,
        'e': 1
    }
    for slowo in lines:
        d = {
            'w': 0,
            'a': 0,
            'k': 0,
            'c': 0,
            'j': 0,
            'e': 0
        }

        for litera in slowo:
            if litera in d.keys():
                d[litera] += 1

        ilosc_slow = d['w']

        for key in d.keys():
            if d[key] // wakacje[key] < ilosc_slow:
                ilosc_slow = d[key] // wakacje[key]

        f_wyn2.write(f'{str(ilosc_slow)} ')
        print(ilosc_slow)
    f_wyn2.close()


# zad2()

def zad3():
    f_wyn3 = open('./wyniki4_3.txt', 'wt', encoding='UTF-8')
    w = 'wakacje'

    for slowo in lines:
        wycinek = ''
        ile_wykreslic = 0
        for litera in slowo:
            szukana_litera = ''
            if wycinek == '':
                szukana_litera = 'w'
            elif wycinek == 'wakacje':
                wycinek = ''
                szukana_litera = 'w'
            else:
                szukana_litera = w.split(wycinek)[1][0]

            if litera == szukana_litera:
                wycinek += litera
                print(wycinek)
            else:
                ile_wykreslic += 1
                print(ile_wykreslic)
        if wycinek != 'wakacje':
            f_wyn3.write(f'{str(ile_wykreslic + len(wycinek))} ')
        else:
            f_wyn3.write(f'{str(ile_wykreslic)} ')


zad3()
