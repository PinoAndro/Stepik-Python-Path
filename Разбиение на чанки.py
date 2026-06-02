import math

def chunked(s, n):
    lst = []
    for i in range(math.ceil(len(s) / n)):
        lst.append([])
        lst[i]= s[i * n:n * (i + 1)]
    return lst

s = input().split()
n = int(input())
print(chunked(s, n))
