# dfs

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = []



N = int(input())

arr = [list(input()) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

def dfs(x, y):    
    num = 1 

    visit[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if visit[nx][ny] == 0 and arr[nx][ny] == '1':
                num += dfs(nx, ny)

    return num

for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 and arr[i][j] != '0':
            result.append(dfs(i, j))

print(len(result))
result.sort()
for i in result:
    print(i)
    
   

#####################################


# bfs

from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):

    num = 0
    
    queue = deque()    
    queue.append((x, y))
    visit[x][y] = 1
    
    while queue:
        v = queue.popleft()
        num += 1
        #print(v)        

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visit[nx][ny]==0 and arr[nx][ny] == '1':
                    queue.append((nx, ny))
                    visit[nx][ny] = 1

    return num


result = []


N = int(input())

arr = [list(input()) for _ in range(N)]
visit = [[0]*N for _ in range(N)]


for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 and arr[i][j] != '0':
            result.append(bfs(i, j))

print(len(result))
result.sort()
for i in result:
    print(i)
