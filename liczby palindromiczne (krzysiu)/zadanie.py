f = open('./dane.txt')
lines = f.read().strip().split('\n')


def czy_palindrom(l: str):
    if len(l) == 1:
        return True
    for i in range(len(l) // 2 + 1):
        if l[i] != l[len(l) - i - 1]:
            return False
    return True


def dec_to_custom(n: int, podstawa: int):
    b = []
    szesnastkowy = ['A', 'B', 'C', 'D', 'E', 'F']
    if n == 0:
        return '0'
    while n > 0:
        reszta = n % podstawa
        if podstawa == 16 and reszta > 9:
            b.append(szesnastkowy[reszta - 10])
        else:
            b.append(str(reszta))
        n //= podstawa
    return "".join(b[::-1])


def zad1():
    ile = 0
    for line in lines:
        b = dec_to_custom(int(line), 2)
        if czy_palindrom(b):
            ile += 1
    print(f'1.1: {str(ile)}')


zad1()


def zad2():
    ile = 0
    for line in lines:
        b = dec_to_custom(int(line), 16)
        if czy_palindrom(b):
            ile += 1
    print(f'1.2: {str(ile)}')


zad2()


def zad3():
    systemy = {
        '2': 0,
        '4': 0,
        '8': 0,
        '16': 0
    }
    for line in lines:
        for key in systemy.keys():
            konwersja = dec_to_custom(int(line), int(key))
            if czy_palindrom(konwersja):
                systemy[key] += 1
    print(f'1.3: {str(systemy)}')


zad3()


def zad4():
    liczby = {}
    for line in lines:
        ile_p = 0
        palindormy = []
        for key in ['2', '4', '8', '16']:
            konwersja = dec_to_custom(int(line), int(key))
            if czy_palindrom(konwersja):
                ile_p += 1
                palindormy.append(key)
        liczby[line] = {
            'ile_p': ile_p,
            'palindormy': palindormy
        }
    max_p = 0
    for key in liczby.keys():
        if liczby[key]['ile_p'] > max_p:
            max_p = liczby[key]['ile_p']
    ile = 0
    print('1.4:')

    for key in liczby.keys():
        ile_p = liczby[key]['ile_p']
        if ile_p == max_p and ile < 4:
            ile += 1
            print(f'{key} {ile_p} {str(liczby[key]["palindormy"])}')


zad4()
