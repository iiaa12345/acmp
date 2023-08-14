n = int(input())
b = []

for i in range(n):
    x = list(map(int, input().split()))
    b.append(x)

b.sort(key=lambda t: t[0] * 3600 + t[1] * 60 + t[2])

for i in range(n):
    print(b[i][0], b[i][1], b[i][2])
