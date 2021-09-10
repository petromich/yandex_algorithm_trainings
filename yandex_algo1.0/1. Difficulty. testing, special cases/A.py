a, b = input().split()
troom, tcond = int(a), int(b)
mode = input()
ans = troom
if mode == 'heat' and tcond > troom:
    ans = tcond
elif mode == 'freeze' and tcond < troom:
    ans = tcond
elif mode == 'auto':
    ans = tcond
print(ans)