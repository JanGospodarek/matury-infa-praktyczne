def dec_to_bin(a, n):
    A = [None] * (n)
    print(A)
    i = n - 1
    while a > 0:
        A[i] = a % 2
        a = a // 2
        i = i - 1
    return A


def znajdz(x, y, k):
    binX = dec_to_bin(x, k)
    binY = dec_to_bin(y, k)
    ile_par = 0
    for i in range(k):
        if binY[i] == binX[i]:
            ile_par += 1
        else:
            break
    return k - ile_par


print(znajdz(16, 30, 5))
