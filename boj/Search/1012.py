import sys
sys.setrecursionlimit(10**6)


T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def snake(x, y, r, c):    
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if 0 <= tx < r and 0 <= ty < c and visit[tx][ty] == 0:
            visit[tx][ty] = 1

            if arr[tx][ty] == 1:
                snake(tx, ty, r, c)

    return
                




for t in range(T):
    M, N, K = map(int, input().split())

    arr = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    result = 0

    
    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    

    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0 and arr[i][j] == 1:
                snake(i, j, N, M)
                result += 1

    print(result)
