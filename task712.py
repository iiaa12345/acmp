w, h, n = map(int, input().split())
st = 0
en = max(w, h) * n

min_ans = en
while en >= st:
    mid = (st + en) // 2
    if (mid // w) * (mid // h) >= n:
        min_ans = mid
        en = mid - 1
    else:
        st = mid + 1

print(min_ans)
