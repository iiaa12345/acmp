b = list(input())
a = [i for i in range(len(b))]

while True:
    t = []
    for i in range(len(b)):
        t.append(b[a[i]])

    print("".join(t))

    i = len(b) - 2
    while i >= 0:
        if a[i] < a[i + 1]:
            break
        i -= 1

    if i < 0:
        break

    j = i + 1
    min_j = None
    while j  < len(b):
        if min_j == None:
            if a[j] > a[i]:
                min_j = j
        else:
            if a[j] > a[i] and a[j] < a[min_j]:
                min_j = j
        j += 1
    
    a[i], a[min_j] = a[min_j], a[i]
    
    k = i + 1
    l = len(b) - 1
    while l > k:
        a[k], a[l] = a[l], a[k]
        k += 1
        l -= 1
