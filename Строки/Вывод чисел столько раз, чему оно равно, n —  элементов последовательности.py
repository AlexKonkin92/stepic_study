a =int(input())
c = 0
b = []
g = 0
for i in range(1, a + 1):
    b = b + [i] * i
    if i == a:
            g = b[:a]
            print(*g, end = ' ')