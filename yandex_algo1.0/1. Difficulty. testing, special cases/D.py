a = int(input())
b = int(input())
c = int(input())
if c < 0:
    print('NO SOLUTION')
elif a == 0:
    if b >= 0 and b == c * c:
        print('MANY SOLUTIONS')
    else:
        print('NO SOLUTION')
elif (c * c - b) / a * a + b < 0 or ((c * c - b) / a).is_integer() == False:
    print('NO SOLUTION')
else:
    print(int((c * c - b) / a))
    
