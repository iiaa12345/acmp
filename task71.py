n = int(input())
a = list(map(int, input().split()))
b = [0] * n
min_diff = None

while True:
    sum1 = 0
    sum2 = 0
    for i in range(n):
        if b[i] == 0:
            sum1 += a[i]
        else:
            sum2 += a[i]

    if min_diff == None:
        min_diff = max(sum1, sum2) - min(sum1, sum2)
    elif max(sum1, sum2) - min(sum1, sum2) < min_diff:
        min_diff = max(sum1, sum2) - min(sum1, sum2)

    i = n - 1
    while i >= 0:
        if b[i] == 1:
            b[i] = 0
        else:
            b[i] = 1
            break
        i -= 1
    if i < 0:
        break

print(min_diff)
