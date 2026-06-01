def pascal(num_str):
    lst = [1]
    lst_new = []
    step = 0
    while True:
        a = (num_str + 1) // 2 + (num_str + 1) % 2
        for _ in range(a):
            lst.append(1)
            step += 1
            window = lst[:step][step - 1] + lst[:step][step]
            print(step)  
            for _ in range(a - 1):
                lst_new.append(window)
                step += 1
            print(lst_new)
        lst_new = lst.copy()
        print(lst)
        print(lst_new)
        break
        
        
            
n = int(input())
pascal(n)



