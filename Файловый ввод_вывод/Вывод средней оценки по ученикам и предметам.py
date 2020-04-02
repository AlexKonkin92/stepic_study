#Петров;85;92;78
#Сидоров;100;88;94
#Иванов;58;72;85
#85.0
#94.0
#71.666666667
#81.0 84.0 85.666666667

with open(r'C:\Users\79851\PycharmProjects\Alex\venv\GitHub\stepic_study\dataset_3363_4.txt','r') as inf:
    d = []
    for line in inf:
        line = line.replace(';', ' ')
        line = line.strip().split()
        d.append(line[1::])
    d = [[int(i) for i in list] for list in d]
    for i in d:
        c = 0
        for j in i:
            c += j
        print(c / 3)
    for i in range(3):
        c = 0
        for j in range(len(d)):
            c += d[j][i]
        print(c / len(d), end=' ')