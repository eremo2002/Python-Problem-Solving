# using binary_search
def binary_search(arr, target, start, end):
    if start > end:
        return 0
    
    mid = (start+end)//2

    if arr[mid]==target:
        return 1
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)


N, M = map(int, input().split())

a = [input() for _ in range(N)]
b = [input() for _ in range(M)]

a.sort()

res = []

for i in b:
    if binary_search(a, i, 0, len(a)-1) == 1:
        res.append(i)

res.sort()
print(len(res))
for i in res:
    print(i)








# using Counter
from collections import Counter

N, M = map(int, input().split())

arr = list(input() for _ in range(N+M))


counter = Counter(arr)
counter = dict(counter)
values = list(counter.values())
print(len(values)-values.count(1))

counter_sorted = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

for i in counter_sorted:
    if i[1] < 2:
        break
    else:
        print(i[0])
