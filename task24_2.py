n, m = list(map(int, input().split()))
cnt = 0

if m == 0:
    print(1)
elif m == 1:
    print(n)    
else:
    i = 0
    while True:
        l = (i + 1) * (m - 1) + 1
        if l > n:
            break
        cnt += n - l + 1
        i += 1

    print(cnt)
