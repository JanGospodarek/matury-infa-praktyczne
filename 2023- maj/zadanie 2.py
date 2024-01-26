def oblicz_bloki(n):
    poprzednia = n % 2
    bloki = 1
    n = n // 2
    while n > 0:
        reszta = n % 2
        if reszta != poprzednia:
            poprzednia = reszta
            bloki += 1
        n = n // 2
    print(bloki)


# oblicz_bloki(67)
f = open('./Dane_2305/bin.txt')
lines = f.read().strip().split('\n')


def zad2():
    ile = 0
    for line in lines:
        bloki = 1
        for i in range(1, len(line)):
            if line[i - 1] != line[i]:
                bloki += 1
        if bloki <= 2:
            ile += 1
    print(ile)


# zad2()
def bin_to_dec(b: str):
    k = 0
    suma = 0
    for i in range(len(b) - 1, -1, -1):
        suma += int(b[i]) * (2 ** k)
        k += 1
    return suma


def zad3():
    max_d = 0
    max_b = ''
    for line in lines:
        d = bin_to_dec(line)
        if d > max_d:
            max_d = d
            max_b = line
    print(max_b)


# zad3()
def dec_to_bin(dec: int):
    bin = []
    while dec > 0:
        bin.append(str(dec % 2))
        dec = dec // 2
    return "".join(bin[::-1])


def zad5():
    with open('./wyniki2_5.txt', 'wt', encoding='utf-8') as f_odp:
        for line in lines:
            dec = bin_to_dec(line)
            polowa = dec // 2
            bin_pol = dec_to_bin(polowa)
            roznica = len(line) - len(bin_pol)
            uzupelnienie = '0' * roznica
            bin_pol = uzupelnienie + bin_pol
            xor = []
            for i in range(len(line)):
                if (line[i] == '0' and bin_pol[i] == '1') or (line[i] == '1' and bin_pol[i] == '0'):
                    xor.append('1')
                else:
                    xor.append('0')
            xor_str = "".join(xor)
            f_odp.write(f'{xor_str} \n')


zad5()
