n = int(input())
a = list(map(int, input().split()))
b = [0]
i = 0

if n == 2:
    b.append(abs(a[i] - a[i - 1]) + b[i - 1])
else:
    for i in range(1, n):
        if i == 1:
            b.append(abs(a[i] - a[i - 1]) + b[i - 1])
        elif abs(a[i] - a[i - 1]) + b[i - 1] <= 3 * abs(a[i] - a[i - 2]) + b[i - 2]:
            b.append(abs(a[i] - a[i - 1]) + b[i - 1])
        else:
            b.append(3 * abs(a[i] - a[i - 2]) + b[i - 2])

print(b[n - 1])
