k1, m, k2, p2 , n2 = input().split()
k1 = int(k1)
m = int(m)
k2 = int(k2)
p2 = int(p2)
n2 = int(n2)

def SolNeq(a, b):
    ans = []
    for i in range(int(b) - int(a) + 1):
        if b > int(a) + i >= a:
            ans.append(int(a) + i)
    if ans == []:
        return -1
    else:
        return ans
if n2 > m:
    print(-1, -1)
else:
    if p2 == 1 and n2 == 1:
        if k1 <= k2:
            print(1, 1)
        elif m == 1:
            print(0, 1)
        elif k2 * m >= k1:
            print(1, 0)
        else:
            print(0, 0)

    else:
        l = SolNeq(k2 / (m*(p2-1)+n2), k2 / (m*(p2-1)+n2-1))
        if l == -1:
            print(-1, -1)
        else:
            p1v = []
            n1v = []
            for i in range(len(l)):
                for j in range(m):
                    if SolNeq((k1 / l[i] - j - 1) / m + 1, (k1 / l[i] - j) / m + 1) != -1:
                        if len(SolNeq((k1 / l[i] - j - 1) / m + 1, (k1 / l[i] - j) / m + 1)) == 1:
                            p1v.append(SolNeq((k1 / l[i] - j - 1) / m + 1, (k1 / l[i] - j) / m + 1)[0])
                        else:
                            p1 = 0
                        n1v.append(j+1)
            s = list(set(n1v))
            p1v = list(set(p1v))
            if p1v == [] and n1v == []:
                print(-1, -1)
            else:
                if len(p1v) == 1:
                    p1 = p1v[0]
                else:
                    p1 = 0
                if len(s) == 1:
                    p2 = s[0]
                else:
                    p2 = 0
                print(p1, p2)
