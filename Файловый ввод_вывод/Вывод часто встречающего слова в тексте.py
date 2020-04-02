a = 'ABc a abc'
#inf =  open (r'C:\Users\79851\PycharmProjects\Alex\venv\GitHub\stepic_study\dataset_3363_3.txt','r')
#a =  inf.read().replace('\n', ' ').lower().split()
#inf.close()
#a.sort()
b = {}
c = []
g = 0
for i in a:#проверям в ключах значение
  if i not in b.keys():
    b[i] = len(i)#если нет, то добавляем
g = max(b.values())
for key, value in b.items():
    if value == g:
        c.append(key)
        c.append(value)
        break
print(c)
#with  open (r'C:\Users\79851\PycharmProjects\Alex\venv\GitHub\stepic_study\file.txt','w') as ouf:
#    ouf.write(c[0] + ' ' + str(c[1]))#вывод строки
#    ouf.close()
