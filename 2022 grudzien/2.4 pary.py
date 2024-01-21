f = open('./Dane_2212/pary.txt')
lines = f.read().strip().split('\n')


def rysuj(x, y, g_x, g_y):
    if x == y:
        print(g_x, g_y)
    if 2 * x <= y:
        rysuj(2 * x, y, g_x, g_y)
    if 2 * x + 1 <= y:
        rysuj(2 * x + 1, y, g_x, g_y)


for line in lines:
    arr = line.split(' ')
    x = int(arr[0])
    y = int(arr[1])
    rysuj(x, y, x, y)
