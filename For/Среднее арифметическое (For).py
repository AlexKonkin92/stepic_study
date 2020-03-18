a = int(input())
b = int(input())
j = 0
z = 0
for i in range(a, b + 1):
        if i % 3 == 0:
            j = j + i
            z = z + 1
print(j / z)