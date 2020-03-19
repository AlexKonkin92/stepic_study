s = 'aaabbcaa'
j = len(s)
p = j - 1
b = 0
g = 0
i = 0
while i != j:
    if i != p:#до предпоследнего символа
        if s[i] == s[i+1]:#проверяем с последующим символом
                    g = g + 1
                    i = i + 1
        else:
                    print(s[i],g+1,sep='',end='')#если не совпадает, то выводим
                    i = i + 1
                    g = 0
    else:
                if s[i] == s[i]:#сравниваем с последним символом
                    g = g + 1
                    print(s[i], g, sep='', end='')
                    break

