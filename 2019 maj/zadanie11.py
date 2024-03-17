t = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]
dd = 10


def znajdz(A, n):
    lewy = 0
    prawy = n
    while lewy < prawy:
        s = (lewy + prawy) // 2
        if A[s] % 2 == 0:
            prawy = s
        else:
            lewy = s + 1
    return A[prawy]


print(znajdz(t, dd))
