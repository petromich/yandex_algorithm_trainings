a1 = input()
a2 = input()
a3 = input()
a4 = input()

def pars(a):
    j = 0
    n = ''
    for i in range(len(a)):
        if a[i].isdigit():
            n += a[i]
            j += 1
    k = int(n)
    if j == 11:
        k = k % 10**10
    elif j == 7:
        k = k + 495*10**7
    return k
if(pars(a1) == pars(a2)):
    print('YES')
else:
    print('NO')
if(pars(a1) == pars(a3)):
    print('YES')
else:
    print('NO')
if(pars(a1) == pars(a4)):
    print('YES')
else:
    print('NO')
