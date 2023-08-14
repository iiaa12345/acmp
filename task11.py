def stair(k, n):
    global mem

    if n in mem:
        return mem[n]
    elif n == 0:
        return 1
    elif n >= 1:
        s = 0
        for i in range(n - k, n):
            if i >= 0:
                s += stair(k, i)
        mem[n] = s
        return s


k, n = list(map(int, input().split()))
mem = {}

print(stair(k, n))
