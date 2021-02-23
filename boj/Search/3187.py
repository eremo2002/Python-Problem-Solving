from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(px, py):
    num_k = 0
    num_v = 0

    q = deque()
    q.append((px, py))
    visited[px][py] = 1

    if arr[px][py] == 'k':
        num_k += 1
    elif arr[px][py] == 'v':
        num_v += 1            

    while q:
        v = q.popleft()     
        
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if 0<=nx<x and 0<=ny<y:
                if arr[nx][ny] != '#' and visited[nx][ny] == 0:       

                    if arr[nx][ny] == 'k':
                        num_k += 1
                    elif arr[nx][ny] == 'v':
                        num_v += 1                    
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    
    
    return (num_k, num_v)

x, y = map(int, input().split())

arr = [list(input()) for _ in range(x)]
visited = [[0]*y for _ in range(x)]

survived_k = 0
survived_v = 0

for i in range(x):
    for j in range(y):
        if visited[i][j] == 0 and arr[i][j] != '#':
            res = bfs(i, j)
            if res[0] <= res[1]:
                survived_v += res[1]
            elif res[0] > res[1]:
                survived_k += res[0]

print(survived_k, survived_v)


        

