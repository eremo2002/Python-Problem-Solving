import sys
from collections import Counter

N = int(input())
arr = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
arr.sort()

print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])

counter = Counter(arr)
cnt = counter.most_common()
cnt.sort(key=lambda x: (-x[1], x[0]))

if len(cnt) == 1:
    print(cnt[0][0])
elif len(cnt) >= 2:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])


print(max(arr) - min(arr))
