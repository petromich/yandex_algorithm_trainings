a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
mins = 0
if((a + c)*max(b, d) < (a + d) * max(b, c)):
    s1 = a + c
    s2 = max(b, d)
    mins = (a + c)*max(b, d)
else:
    s1 = a + d
    s2 = max(b, c)
    mins = (a + d) * max(b, c)
if((b + c)*max(a, d) < mins):
    s1 = b + c
    s2 = max(a, d)
    mins = (b + c)*max(a, d)
if ((b + d) * max(a, c) < mins):
    s1 = b + d
    s2 = max(a, c)
    mins = (b + d) * max(a, c)
print(s1, s2)