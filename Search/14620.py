N = int(input())

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
result = 999999

arr = [list(map(int, input().split())) for _ in range(N)]

def flower(lst):    
    pos = []
    money = 0

    for i in lst:
        x = i // N
        y = i % N

        for j in range(5):
            tx = x + dx[j]
            ty = y + dy[j]

            if 0 <= tx < N and 0 <= ty < N:                           
                pos.append(tx*N + ty)    
                money += arr[tx][ty]

    

    if len(set(pos)) == 15:             
        return money

    else:
        return 999999





for i in range(N*N):
    for j in range(i+1, N*N):
        for k in range(j+1, N*N):
            result = min(result, flower([i, j, k]))




print(result)
