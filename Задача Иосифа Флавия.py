n = int(input())
k = int(input())
alives = [men for men in range(1, n + 1)]
kills_count = 0
i = 0
while len(alives) > 1:
        ind = (-1 + k + i) % (n - kills_count)
        alives.pop(ind)
        i = ind
        kills_count += 1
print(alives[0])
