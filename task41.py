n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 201

for i in range(n):
    cnt[a[i] + 100] += 1

a = []
for i in range(201):
    for j in range(cnt[i]):
        a.append(i - 100)

a = list(map(str, a))
print(' '.join(a))
