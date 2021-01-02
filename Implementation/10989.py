import sys

N = int(input())

arr = [0] * 10001

for i in range(N):    
    s = int(sys.stdin.readline())
    arr[s] += 1

for i in range(10001):
    for j in range(arr[i]):
        print(i)
