import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    ret = 1

    visit[x][y] = 1

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < N and 0 <= ty < 10 and visit[tx][ty] == 0:
            if arr[x][y] != '0' and arr[x][y] == arr[tx][ty]: 
                ret += dfs(tx, ty)
    
    return ret


def bomb(x, y, val):
    visit2[x][y] = 1
    arr[x][y] = '0'

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < N and 0 <= ty < 10 and visit2[tx][ty] == 0:
            if arr[tx][ty] == val:
                bomb(tx, ty, val)            
    return



def down(arr):

    tmp_list = []

    for i in range(10):
        for j in range(N):
            if arr[j][i] != '0':
                tmp_list.append(arr[j][i])

        for k in range(N-1, -1, -1):
            if len(tmp_list) != 0:
                arr[k][i] = tmp_list.pop(-1)
            else:
                arr[k][i] = '0'

        tmp_list.clear()

    return arr


N, K = map(int, input().split())

arr = [list(input()) for _ in range(N)]
visit = [[0 for _ in range(10)] for _ in range(N)]
visit2 = [[0 for _ in range(10)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0

while True:
    flag = False
    
    for i in range(N):
        for j in range(10):
            if visit[i][j] == 0 and arr[i][j] != '0':
                result = dfs(i, j)                
                if result >= K:
                    bomb(i, j, arr[i][j])                    
                    flag = True
    
    if flag == False:
        break
                
    arr = down(arr)

    
    for i in range(N):
        for j in range(10):
            visit[i][j] = 0
            visit2[i][j] = 0
    



for i in range(N):
    for j in range(10):
        print(arr[i][j], end='')
    print()
