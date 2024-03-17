f = open('./Dane_PR2/pary.txt')
lines = f.read().strip().split('\n')


def czy_p(n: int):
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def znajdz_pierwsze(n: int):
    for i in range(1, n // 2 + 1):
        if czy_p(i) and czy_p(n - i):
            return [str(i), str(n - i)]


def zad1():
    for line in lines:
        arr = line.split(" ")
        liczba = int(arr[0])
        if liczba % 2 == 0:
            print(liczba, " ".join(znajdz_pierwsze(liczba)))


# zad1()


def zad2():
    for line in lines:
        arr = line.split(" ")
        slowo = arr[1]
        dl_max = 1
        znak_max = slowo[0]
        dl = 1
        znak = slowo[0]
        for i in range(1, len(slowo)):
            if slowo[i - 1] == slowo[i]:
                dl += 1
            if dl > dl_max:
                dl_max = dl
                znak_max = znak
            if slowo[i - 1] != slowo[i]:
                dl = 1
                znak = slowo[i]
        print(znak_max * dl_max, dl_max)


# zad2()


def cm(para1, para2):
    if para1[0] < para2[0]:
        return True
    if para1[0] == para2[0] and para1[1] < para2[1]:
        return True
    return False


def zad3():
    for line in lines:
        arr = line.split(" ")
        slowo = arr[1]
        liczba = int(arr[0])

        if liczba == len(slowo):
            czy_mniejsza = True

            for line2 in lines:
                arr2 = line2.split(" ")
                slowo2 = arr2[1]
                liczba2 = int(arr2[0])
                if liczba2 == len(slowo2) and slowo2 != slowo:
                    if not cm([liczba, slowo], [liczba2, slowo2]):
                        czy_mniejsza = False
            if czy_mniejsza:
                print(arr)


zad3()
