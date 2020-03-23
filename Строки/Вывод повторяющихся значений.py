s = [int(i) for i in input().split()]
s.sort()
for k in range(len(s)):
        if s.count(s[k])>1 and s[k - 1] != s[k]:
            print(s[k],end=' ')
        elif s.count(s[k])>1 and s[0] == s[-1]:
            print(s[k], end=' ')
            break







