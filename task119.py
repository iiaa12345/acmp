n = int(input())
b = []

for i in range(n):
    h, m, s = list(map(int, input().split()))
    b.append(h * 60 * 60 + m * 60 + s)

b.sort()

for i in range(n):
    h = b[i] // 60 // 60
    m = b[i] // 60 % 60
    s = b[i] % 60
    print(h, m, s)
