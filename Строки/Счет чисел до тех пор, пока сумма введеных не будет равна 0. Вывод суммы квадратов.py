a = int(input())
y = 0
z = 0
while (a + y) != 0:
    y = y + a
    z = z + a**2
    a = int(input())
z = z + a**2
print(z)