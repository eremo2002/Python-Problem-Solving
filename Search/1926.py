from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    stack = deque()
    stack.append((x, y))
    visited[x][y] = 1
    cnt = 0    

    while stack:
        v = stack.pop()
        if arr[v[0]][v[1]] == 1:
            cnt += 1
        
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and arr[nx][ny]==1:
                    stack.append((nx, ny))
                    visited[nx][ny] = 1

    return cnt

    
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

num = 0
area = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and arr[i][j] == 1:
            area = max(area, dfs(i, j))
            num += 1

print(num)
print(area)
