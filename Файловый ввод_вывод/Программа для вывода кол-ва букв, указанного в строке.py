#Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.
inf =  open (r'C:\Users\79851\PycharmProjects\Alex\venv\GitHub\stepic_study\dataset_3363_2.txt','r')
a = inf.readline().strip()
inf.close()
#a = 't12N2c10Q7I14Q14z13Z14d8u18H11f6c4A17h6c1l18i20Y12a2f5R4x16W11r7'
c = ''
g = 1
t = ''
for i in range(len(a)):
    if i != len(a) - 1:
        if '0' <= a[i] <= '9':
            if '0' <= a[i + 1] <= '9':
                c = c + a[i]
                g = g + 1

            else:
                c = c + a[i]
                t = t + a[i - g] * int(c)
                c = ''
                g = 1
    else:
        c = c + a[i]
        t = t + a[i - g] * int(c)
#print(t)
ouf = open(r'C:\Users\79851\PycharmProjects\Alex\venv\GitHub\stepic_study\file.txt','w')
ouf.write(t)
ouf.close()