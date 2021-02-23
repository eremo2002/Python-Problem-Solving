from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))    
    visited[x][y] = 0

    while q:
        v = q.popleft()        
        
        for i in range(6):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if 0<=nx<N and 0<=ny<N:                
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[v[0]][v[1]] + 1
        

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0]*N for _ in range(N)]


bfs(r1, c1)
if visited[r2][c2] == 0:
    print('-1')
else:
    print(visited[r2][c2])
