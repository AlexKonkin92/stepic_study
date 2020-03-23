lst= [int(i) for i in input().split()]
if len(lst) == 1:
        print(lst[0])
else:
    for i in range(len(lst)):
        print(lst[i-1] + lst[i+1-len(lst)], end=' ')