def oblicz(A):
    s = 0
    for i in range(1, len(A)):
        if A[i - 1] != A[i]:
            s += 1
    s += 1
    print(s * 2)


oblicz([3, 3, 3, 2, 2, 1, 1, 1])
