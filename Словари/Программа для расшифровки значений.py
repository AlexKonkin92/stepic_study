#Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
#Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
#на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать
#переданным ключом, и ещё одна строка, которую нужно расшифровать.
#a = abcd
#b = *d%#
#e = abacabadaba
#r = #*%*d*%

a,b,e,r = input().strip(),input().strip(),input().strip(),input().strip()
d,q = {},{}
z,c = [],[]
for i in range(len(a)):
    d[(a+b)[i]] = [(a+b)[i+len(a)]] #делаю ключ - значение для 'e'
    q[(a+b)[i+len(a)]] = [(a+b)[i]]#делаю обратный ключ - значение для 'r'
for i in range(len(e)):
    c.append(d[e[i]][0]) #наполняю список по значениям 'a'
for i in range(len(r)):
    z.append(q[r[i]][0])#наполняю список по значениям 'b'
print(*c,sep='') #*d*%*d*#*d*
print(*z,sep='') #dacabac