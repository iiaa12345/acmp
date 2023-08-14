INF = 1000000

n, s, f = [int(i) for i in input().split()]

g = []
for i in range(n):
    g.append([int(i) for i in input().split()])

v = [True] * n
w = [INF] * (s - 1) + [0] + [INF] * (n - s)

while True:
    min_w = INF
    ind = None
    for i in range(n):
        if v[i] and w[i] < min_w:
            min_w = w[i]
            ind = i

    if ind == None:
        break

    for j in range(n):
        if g[ind][j] >= 0 and ind != j and v[j]:
            w[j] = min(w[j], w[ind] + g[ind][j])

    v[ind] = False

if w[f - 1] == INF:
    print(-1)
else:
    print(w[f - 1])
