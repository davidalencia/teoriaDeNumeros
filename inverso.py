
def inv(n, m):
    for i in range(0,m):
        if (n*i)%m==1:
            return i

print(inv(2, 7))