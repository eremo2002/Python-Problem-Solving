r, c = map(int, input().split())

arr = [list(input()) for _ in range(r)]

flag = False

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# can't install D
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            for k in range(4):
                i2 = i + dx[k]
                j2 = j + dy[k]

                if 0 <= i2 < r and 0<= j2 < c:
                    if arr[i2][j2] == 'S':
                        print("0")
                        flag = True
                        exit(0)

if flag == False:
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'S':
                for k in range(4):
                    i2 = i + dx[k]
                    j2 = j + dy[k]

                    if 0 <= i2 < r and 0 <= j2 < c:
                        if arr[i2][j2] == '.':
                            arr[i2][j2] = 'D'



    print("1")
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end='')
        print()
