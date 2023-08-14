def bag(k, ind, n, wmax, w, p):
    global pmax, ind_max

    wsum = 0
    psum = 0
    for i in ind:
        wsum += w[i]
        psum += p[i]

    if wsum <= wmax and psum >= pmax:
        if psum == pmax:
            if len(ind) < len(ind_max):
                pmax = psum
                ind_max = ind[:]
        else:
            pmax = psum
            ind_max = ind[:]

    if k == n:
        return
    else:
        s1 = set([i for i in range(n)])
        s2 = set(ind)
        for i in list(s1 - s2):
            if wsum + w[i] <= wmax:
                ind.append(i)
                bag(k + 1, ind, n, wmax, w, p)
                ind.remove(i)


n, wmax = list(map(int, input().split()))
w = []
p = []
for i in range(n):
    wi, pi = list(map(int, input().split()))
    w.append(wi)
    p.append(pi)

pmax = 0
ind_max = []

bag(0, [], n, wmax, w, p)

print(len(ind_max), pmax)

ind_max = [i + 1 for i in ind_max]
ind_max = sorted(ind_max)

print(" ".join(list(map(str, ind_max))))
