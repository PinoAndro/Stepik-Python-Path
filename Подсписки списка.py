s = input().split()
lst = []
lst.append([])
slice = 1
for i in range(len(s), 0, -1):
    for j in range(i):
        lst.append(s[j : j + slice])
    slice += 1
print(lst)
