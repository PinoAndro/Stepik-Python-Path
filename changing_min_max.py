s = input().split()
s1 = s.copy()
total = 0
for num in range(len(s1)):
    s1[num] = int(s1[num])
    total += s1[num]
s[s.index(str(total - (total - min(s1))))] = str(max(s1))
s[s1.index(max(s1))] = str(min(s1))
print(' '.join(s))
