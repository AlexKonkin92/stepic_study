# put your python code here

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a!=0 and b!=0 and c!=0 and d!=0 and a<=b and c <= d:
  for k in range (c,d+1):
    print('\t',k,sep='',end='')# имитируем нажатие Tab, число к, пробел, ставим end='', тк если мы этого не сделаем, то по умолчанию он ставится \n, а нам нужно , чтобы всё было на одной строке
  print()# вывести пустое значение, сымитировать нажатие Enter по умолчанию end='\n'
  for g in range(a,b+1):
    print(g,end='\t')
    for y in range(c,d+1):
      print(g*y, end='\t')
    print()
else:
  print('Одно из чисел 0')



