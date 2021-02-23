def dfs(node, arr, visited):

    visited[node] = 1
    

    for i in arr[node]:
        nx = i

        if visited[nx] == 0:            
            dfs(nx, arr, visited)

    return None
 

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [0]*N

new_arr = [[] for i in range(N) ]

for i in arr:
    new_arr[i[0]-1].append(i[1]-1)
    new_arr[i[1]-1].append(i[0]-1)


dfs(0, new_arr, visited)
print(visited.count(1)-1)
