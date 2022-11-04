from math import floor 

def d(x,y):
    return  4900*y-1700*x
    

def binarySearch(n, start, end):
    if start > end:
        return False
    mid = floor((start+end)/2)
    print(f"4900*{mid}-1700*{n}={d(n, mid)}")
    if d(n,mid)==24500:
        return True
    if d(n,mid)>24500:
        return binarySearch(n, start, mid-1)
    else:
        return binarySearch(n, mid+1, end)

for i in range(5_000, 10_000+1):
    print(f"-------------------{i}-------------------")
    if binarySearch(i, 0, i):
        break



