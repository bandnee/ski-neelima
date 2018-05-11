
def pow(dblbase, exp) :

    if exp == 0:
        return 1
    if exp == 1:
        return dblbase
    half = int(exp / 2)
    if exp % 2 == 0 :
        half_pow = pow(dblbase, half)
        res = half_pow * half_pow
    else:
        half_pow = pow(dblbase, half)
        res = half_pow * half_pow * dblbase
    return res


print(pow(2,3))
