class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18

        strings = set(original) | set(changed)
        idx = {}
        rev = []
        for s in strings:
            idx[s] = len(rev)
            rev.append(s)

        m = len(rev)
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            dist[idx[o]][idx[c]] = min(dist[idx[o]][idx[c]], w)

        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        n = len(source)
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue

            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            for s in strings:
                l = len(s)
                if i + l <= n and source[i:i+l] == s:
                    t = target[i:i+l]
                    if t in idx and dist[idx[s]][idx[t]] < INF:
                        dp[i + l] = min(dp[i + l], dp[i] + dist[idx[s]][idx[t]])

        return -1 if dp[n] == INF else dp[n]
