n = int(input())

a = [list(map(int, input())) for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

ck = [0 for _ in range(n)]

def dfs(i, j):
    for way in range(4):
        ii, jj = i + dx[way], j + dy[way]
        if a[ii][jj] == 1:
            dfs(ii, jj)

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            dfs(i, j)
