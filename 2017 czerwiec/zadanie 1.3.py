## zadanie 1.3 (opis w zeszycie od polskiego)

czyjest = [None, False, False, False, True, False, False, False, True, True, False]


def sprawdz(k):
    for i in range(1, len(czyjest)):
        for j in range(i, len(czyjest)):
            if czyjest[i] and czyjest[j] and i + j == k:
                return True
    return False


print(sprawdz(12))
