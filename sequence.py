def fibo(n):
    res = []
    a, b = 0, 1
    while a < n:
        res.append(a)
        a, b = b, a+b
    return res

def natural(n):
    res = []
    a = 1
    while a < n:
        res.append(a)
        a = a + 1
    return res

def squares(n):
    res = []
    a = 1
    while a < n:
        res.append(a*a)
        a = a + 1
    return res

def cubes(n):
    res = []
    a = 1
    while a < n:
        res.append(a*a*a)
        a = a + 1
    return res

