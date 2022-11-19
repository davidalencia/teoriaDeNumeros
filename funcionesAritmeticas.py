def factoresprimos(n):
    i = 2
    factores = []
    while i * i <= n:
        if n % i:
            i = i+ 1
        else:
            n = n // i
            factores.append(i)
    if n > 1:
        factores.append(n)
    return factores

def tau(n):
    return len(factoresprimos(n))

def phi(n):
    factores = factoresprimos(n)
    d = dict.fromkeys(factores, 0)
    for i in factores:
        d[i] = d[i] + 1
    s = n
    for p, a in d.items():
        s *= (1-(1/p)) #s*(pow(p, a+1)-1)//(p-1)
    return round(s)

def sigma(n):
    factores = factoresprimos(n)
    d = dict.fromkeys(factores, 0)
    for i in factores:
        d[i] = d[i] + 1
    print(d)
    s = 1
    for p, a in d.items():
        s = s*(pow(p, a+1)-1)/(p-1)
    return s
