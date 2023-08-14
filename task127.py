n = int(input())
g = []
for i in range(n):
    g.append([int(i) for i in input().split()])
st, en = [int(i) - 1 for i in input().split()]
w = [1000 for i in range(st)] + [0] + [1000 for i in range(n - st - 1)]
v = []
q = [st]

while len(q) > 0:
    c = q.pop()
    if c not in v:
        v.append(c)
        for i in range(len(g[c])):
            if i not in v and g[c][i] > 0 and i not in q:
                q.insert(0, i)
                w[i] = min(w[i], w[c] + 1)

if w[en] == 1000:
    print(-1)
else:
    print(w[en])
