a = int(input())
curr = 0
next_ = 1
for i in range(a - 1): 
    print(next_ + curr, end = " ")
    curr, next_ = next_, curr + next_
