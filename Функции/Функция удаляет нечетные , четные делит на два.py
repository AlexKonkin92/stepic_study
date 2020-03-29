def modify_list(l):
    for i in range(len(l)-1,-1,-1):
        if l[i] % 2 != 0:
            l.remove(l[i])
    b = len(l)
    for i in range(b):
        a = l[0] // 2
        l.append(a)
        l.remove(l[0])
    return l
lst = [1, 3,4, 5, 7]
print(modify_list(lst))