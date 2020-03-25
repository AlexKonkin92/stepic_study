a = [int(i) for i in input().split()]
b = int(input())
if a.count(b) > 0:
    for i in range(len(a)):
        if a[i] == b:
            print(i, end = ' ')
else:
    print('Отсутствует')