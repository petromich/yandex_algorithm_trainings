a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

def zero(b, c, d, e, f):
    if b == 0:
        if e == 0:
            if c == 0:
                if d == 0:
                    if f == 0:
                        print(5)
                    else:
                        print(0)
                else:
                    print(4, f / d)
            elif d == 0:
                print(3, f / c)
            else:
                print(1, -c / d, f / d)
        else:
            print(0)
    elif c == 0:
        if d == 0:
            if f == 0:
                print(4, e / b)
            else:
                print(0)
        elif f / d == e / b:
            print(4, e / b)
        else:
            print(0)
    else:
        print(2, f / c - d / c * e / b, e / b)

if a == 0:
    zero(b, c, d, e, f)
elif c == 0:
    zero(d, a, b, f, e)
else:
    zero(b - d / c * a, c, d, e - f / c * a, f)



