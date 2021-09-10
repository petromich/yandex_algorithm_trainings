a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
ans = 0
if b >= c:
    while a >= b:
        ans += (a // b) * (b // c)
        a = a % b + (b % c) * (a // b)
print(ans)
