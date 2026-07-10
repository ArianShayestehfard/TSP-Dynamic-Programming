def tsp(dist):
    n = len(dist)
    dp = [[float('inf')]*n for _ in range(1<<n)]
    parent = [[-1]*n for _ in range(1<<n)]
    dp[1][0] = 0

    for mask in range(1<<n):
        for u in range(n):
            if not (mask & (1<<u)):
                continue
            for v in range(n):
                if mask & (1<<v):
                    continue
                cost = dp[mask][u] + dist[u][v]
                if cost < dp[mask|(1<<v)][v]:
                    dp[mask|(1<<v)][v] = cost
                    parent[mask|(1<<v)][v] = u

    full = (1<<n)-1
    best = float('inf')
    last = 0
    for i in range(1,n):
        if dp[full][i] + dist[i][0] < best:
            best = dp[full][i] + dist[i][0]
            last = i

    path = []
    mask = full
    cur = last
    while cur != -1:
        path.append(cur)
        prev = parent[mask][cur]
        mask ^= (1<<cur)
        cur = prev
    path.append(0)
    path.reverse()
    return best, path

dist = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]

c,p = tsp(dist)
print(c,p)