## teoria


def oblicz1(n):
    if n == 1 or n == 2:
        return 1
    f1 = 1
    f2 = 1

    for i in range(3, n + 1):
        temp = f2
        f2 = f1 + f2
        f1 = temp
    return f2


print(oblicz1(17))


# ponieważ algorytm iteracyjny ma znłożoność liniową
# algorytm rekurencyjny ma złożoność wykładniczą od n

def rekur(n):
    if n == 1 or n == 2:
        return 1
    elif n % 2 == 0:

        i = n / 2 + 1
        k = n / 2 - 1

        return rekur(i) ** 2 - rekur(k) ** 2
    else:
        
        i = (n + 1) / 2
        k = (n + 1) / 2 - 1

        return rekur(i) ** 2 + rekur(k) ** 2


print(rekur(17))
