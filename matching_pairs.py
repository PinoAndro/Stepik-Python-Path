s = input().split()
len_s = len(s)
s1 = s
count = 0
for i in range(len(s1)):
    for j in s1:
        while j in s:
            count += s.count(j)
            del s[s.index(j)]
print(count - len_s)
