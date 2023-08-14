k, n = list(map(int, input().split()))
a = [1]

for i in range(1, n + 1):
    s = 0
    for j in range(1, k + 1):
        if i - j >= 0:
            s += a[i - j]
    a.append(s)

print(a[n])
