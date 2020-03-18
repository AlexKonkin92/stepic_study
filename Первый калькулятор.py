a=float (input())
b=float (input())
c=input()
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/' and b>0:
    print(a/b)
elif c=='mod' and b>0:
    print(a%b)
elif c=='pow':
    print(a**b)
elif c=='div' and b>0:
    print(a//b)
elif (c=='mod' or c=='/' or c=='div') and b == 0:
    print('Деление на 0!')
else:
    print('Такой операции нет!')