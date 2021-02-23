from collections import deque

def new_array():
    return [0]*(N+1)

def bfs(x):
    q = deque()
    q.append(x)

    visited[x] = 0

    while q:
        v = q.popleft()

        for i in graph[v]:
            nx = i
            if visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[v] + 1
            
    return None



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]

visited = new_array()

for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

res = []
for i in range(1, N+1):
    bfs(i)
    kevin = 0
    
    for j in range(1, N+1):
        if i != j:
            kevin += visited[j]

    res.append((i, kevin))

    visited = new_array()

res.sort(key=lambda x: (x[1], x[0]))
print(res[0][0])
