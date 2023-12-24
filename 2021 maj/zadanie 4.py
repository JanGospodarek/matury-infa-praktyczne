f = open('./DANE_2105/instrukcje.txt')
lines = f.read().strip().split('\n')
# print(lines)
napis = ""

for line in lines:
    instrukcja = line.split(' ')[0]
    value = line.split(' ')[1]
    napis_arr = list(napis)
    if instrukcja == "DOPISZ":
        napis += value
    elif instrukcja == "USUN":
        napis_arr.pop()
        napis = "".join(napis_arr)
    elif instrukcja == "ZMIEN":
        napis_arr[-1] = value
        napis = "".join(napis_arr)
    elif instrukcja == "PRZESUN":
        k = 0
        for i, litera in enumerate(list(napis)):
            if litera == value and k == 0:
                nowa_litera = ""
                if ord(litera) == 90:
                    nowa_litera = "A"
                else:
                    nowa_litera = chr(ord(litera) + 1)
                napis_arr[i] = nowa_litera
                napis = "".join(napis_arr)
                k += 1


# print(napis)


def zad2():
    najdl = 1
    max_instr = ""
    dl = 1
    for i in range(1, len(lines)):
        instrukcja1 = lines[i - 1].split(' ')[0]
        instrukcja2 = lines[i].split(' ')[0]
        if instrukcja1 == instrukcja2:
            dl += 1
        if instrukcja1 != instrukcja2:
            dl = 1
        if dl > najdl:
            najdl = dl
            max_instr = instrukcja1
    print(najdl, max_instr)


# zad2()
def zad3():
    instr = {}
    for line in lines:
        instrukcja = line.split(' ')[0]
        value = line.split(' ')[1]
        if instrukcja == "DOPISZ":
            if value in instr.keys():
                instr[value] += 1
            else:
                instr[value] = 1
    s_instr = sorted(instr.items(), key=lambda x: x[1], reverse=True)
    print(s_instr)


zad3()


def zad4():
    print(napis)


zad4()
