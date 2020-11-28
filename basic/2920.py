a = list(map(int, input().split(' ')))

asc = True
des = True


for i in range(0, 7):
    if a[i] < a[i+1]:
        des = False
    elif a[i] > a[i+1]:
        asc = False


if asc:
    print('ascending')
elif des:
    print('desceding')
else:
    print('mixed')

