#На вход программе первой строкой передаётся количество dd известных нам слов
#после чего на dd строках указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.
#Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.


a = int(input())
s,e = {},[]
for i in range(a):
    b = input().lower().strip()
    e.append(b)
w = int(input())
for i in range(w):
    c = input().lower().strip().split()
    for i in c:
        s[i] = i
for i in e:
    if i in s.keys():
        del s[i]
for k,v in s.items():
    print(*v,sep='', end='\n')