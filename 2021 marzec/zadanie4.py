f = open('./Dane_2103/galerie.txt')
lines = f.read().strip().split('\n')
f_lines = []
for line in lines:
    splitted = line.split(' ')
    f_lines.append({'kraj': splitted[0], 'miasto': splitted[1], 'wymiary': splitted[2:]})


# print(f_lines)


def zad1():
    # kraje=[]
    # for line in f_lines:
    #     kraje.append(line['kraj'])
    # kraje=list(set(kraje))
    zbior = {}
    for line in f_lines:
        if line['kraj'] in zbior:
            zbior[line['kraj']] += 1
        else:
            zbior[line['kraj']] = 1
    print(zbior)


# zad1()

def zad2():
    zbior = {}
    for line in f_lines:
        powierzchnia = 0
        wymiary = line['wymiary']
        ile_lokali = 0
        for i in range(1, len(wymiary), 2):
            wym1 = int(wymiary[i - 1])
            wym2 = int(wymiary[i])
            if wym1 != 0 and wym2 != 0:
                ile_lokali += 1
                powierzchnia += (wym1 * wym2)
        zbior[line['miasto']] = f'{str(powierzchnia)} {str(ile_lokali)}'
    print(zbior)
    max_m = ''
    max_p = 0
    min_m = list(zbior.keys())[0]
    min_p = int(zbior[list(zbior.keys())[0]].split(' ')[0])
    for key in zbior.keys():
        powierzchnia = int(zbior[key].split(' ')[0])
        if powierzchnia > max_p:
            max_p = powierzchnia
            max_m = key
        if powierzchnia < min_p:
            min_p = powierzchnia
            min_m = key
    print(max_m, max_p, min_m, min_p)


zad2()


def zad3():
    zbior = {}
    for line in f_lines:
        powierzchnie = []
        wymiary = line['wymiary']
        for i in range(1, len(wymiary), 2):
            wym1 = int(wymiary[i - 1])
            wym2 = int(wymiary[i])
            if wym1 != 0 and wym2 != 0:
                powierzchnie.append(wym1 * wym2)
        zbior[line['miasto']] = len(set(powierzchnie))
    s_zb = sorted(zbior.items(), key=lambda x: x[1])
    print(s_zb)


zad3()
