tablica = []
for i in range(1, 10001):
    tablica.append({'number': i, 'happy': True})


def oblicz():
    i = 0
    while i < len(tablica):
        if tablica[i]['happy']:
            if i == 0:
                for j in range(len(tablica)):
                    if tablica[j]['number'] % 2 == 0:
                        tablica[j]['happy'] = False
            else:
                k = tablica[i]['number']
                j = 0
                r = 0
                while r < len(tablica):
                    if tablica[r]['happy']:
                        if (j + 1) % k == 0:
                            tablica[r]['happy'] = False
                        j += 1
                    r += 1
        i += 1
    print('obliczono tablicę')


oblicz()
f = open('./dane.txt')
lines = f.read().strip().split('\n')


def zad1():
    ile = 0
    for line in lines:
        number = int(line)
        if tablica[number - 1]['happy']:
            ile += 1
    print(ile)


zad1()


def zad2():
    max_dl = 1
    max_pierwszy = int(lines[0])
    dl = max_dl
    pierwszy = max_pierwszy

    for line in lines:
        number = int(line)
        if tablica[number - 1]['happy']:
            dl += 1
            if dl == 1:
                pierwszy = number
        else:
            dl = 0
        if dl > max_dl:
            max_dl = dl
            max_pierwszy = pierwszy
    print(max_pierwszy, max_dl)


zad2()
