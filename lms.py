class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]

        def row_sum(r, c1, c2):
            return row[r][c2] - row[r][c1]

        def col_sum(c, r1, r2):
            return col[r2][c] - col[r1][c]

        max_k = min(m, n)

        for k in range(max_k, 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row_sum(i, j, j + k)

                    ok = True

                    for r in range(i, i + k):
                        if row_sum(r, j, j + k) != target:
                            ok = False
                            break

                    for c in range(j, j + k):
                        if col_sum(c, i, i + k) != target:
                            ok = False
                            break

                    if not ok:
                        continue

                    d1 = d2 = 0
                    for x in range(k):
                        d1 += grid[i + x][j + x]
                        d2 += grid[i + x][j + k - 1 - x]

                    if d1 == target and d2 == target:
                        return k

        return 1
