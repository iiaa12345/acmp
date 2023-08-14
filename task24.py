n, m = list(map(int, input().split()))
a = [0] * n
cnt = 0

while True:
    j = None
    d1 = None
    d2 = None
    fl = False
    if a.count(1) == m:
        for i in range(n):
            if a[i] == 1:
                if j != None:
                    d2 = d1
                    d1 = j - i
                if d2 != None and d2 != d1:
                    fl = True
                    break
                j = i
        if fl == False:
            cnt += 1

    i = n - 1
    while i >= 0:
        if a[i] == 0:
            a[i] = 1
            break
        else:
            a[i] = 0
        i -= 1
    if i < 0:
        break
                    
print(cnt)
