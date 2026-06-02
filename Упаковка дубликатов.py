s = input()
s1 = []
s = s.replace(" ", "")
sublist = [[]]
idx = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        sublist[idx].append(s[i])
    else:
        sublist.append([])
        sublist[idx].append(s[i - 1])
        idx += 1
sublist[-1].append(s[-1])
print(sublist)
