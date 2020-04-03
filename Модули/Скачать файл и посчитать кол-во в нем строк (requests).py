import requests
inf =  open (r'C:\Users\79851\PycharmProjects\Alex\venv\GitHub\stepic_study\dataset_3378_2.txt','r')#читаем файл
dicta =  inf.read().strip()#считываем ссылку
r = requests.get(dicta)#проходим по ссылке
a = 0
for line in r.text.splitlines():#считываем каждую строку в текстовом формате
    a = a + 1
print(a)