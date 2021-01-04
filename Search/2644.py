n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

arr = [list(map(int, input().split())) for _ in range(m)]
visited = [-1]*(n+1)

graph = [[] for _ in range(n+1)]

for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])


def dfs(x, target):    
    
    for i in graph[x]:
        nx = i

        if visited[nx] == -1:
            visited[nx] = visited[x]+1
            dfs(nx, target)
        
    return None

dfs(p1, p2)

if visited[p2] == -1:
    print(-1)
else:
    print(visited[p2]+1)

