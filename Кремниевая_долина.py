n = int(input())
fridges = [input() for _ in range(n)]
for i in range(len(fridges)):
    fridge = fridges[i]
    fridge = ''.join([char for char in fridge if not char.isdigit()])
    if fridge == "anton" or "anton" in fridge:
        print(i + 1, end=" ")
        continue
    name_from_fridge = ''
    for j in "anto":
        for k in range(len(fridge)):
            if name_from_fridge == "anto" and fridge[k] == "o" and "n" in fridge[k:] and fridge.count("n") > 1:
                name_from_fridge += "n"
            if fridge[k] in name_from_fridge:
                continue
            if fridge[k] == j:
                name_from_fridge += fridge[k]
        if name_from_fridge == 'anton':
            print(i + 1, end=" ")
