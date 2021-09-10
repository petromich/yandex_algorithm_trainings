a = int(input())
b = int(input())
m = int(input())
n = int(input())

first_min = m + (m - 1) * a
first_max = m + (m + 1) * a
second_min = n + (n - 1) * b
second_max = n + (n + 1) * b
if first_min > second_max or second_min > first_max:
    print(-1)
else:
    print(max(first_min, second_min), min(first_max, second_max))
