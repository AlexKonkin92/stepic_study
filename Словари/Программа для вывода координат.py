#Для этого программисты просят вас написать программу, которая выведет точку, в которой окажется черепашка после всех команд.
#Для простоты они решили считать, что движение начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.
#Программе подаётся на вход число команд nn, которые нужно выполнить черепашке, после чего
#n строк с самими командами. Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки. Все координаты целочисленные.

a = 0
b = 0
e = {}
f = int(input())
for i in range(f):
    c = input().strip().split()
    if c[0] in e:
        e[c[0]].append(c[1])
    else:
        e[c[0]] = []
        e[c[0]].append(c[1])
if 'север' in e.keys():
    for i in e['север']:
        b = b + int(i)
if 'юг' in e.keys():
    for i in e['юг']:
        b = b - int(i)
if 'восток' in e.keys():
    for i in e['восток']:
        a = a + int(i)
if 'запад' in e.keys():
    for i in e['запад']:
        a = a - int(i)
print(a,b)