def greedyknapsack(W, w, v):
    vw = []
    for i in range(len(w)):
        vw.append((v[i]/w[i]))
    maxben = 0
    while(v):
        ins = vw.index(max(vw))
        maxben += v[ins]
        W -= w[ins]
        if W <= 0:
            maxben -= v[ins]
            W += w[ins]
            v.pop(ins)
            vw.pop(ins)
            w.pop(ins)
            continue
        v.pop(ins)
        vw.pop(ins)
        w.pop(ins)
    return maxben

W = int(input())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
print(greedyknapsack(W, w, v))