a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if (max(a,b) >= max(d,e) and min(a,b) <= min(d,e)) or (max(a,c) >= max(d,e) and min(a,c) <= min(d,e)) or (max(c,b) >= max(d,e) and min(c,b) <= min(d,e)):
    print('YES')
else:
    print('NO')

