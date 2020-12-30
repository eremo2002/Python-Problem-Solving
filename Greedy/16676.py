'''
0~10 => 1
11 => 2
12~110 => 2
111 => 3
...

0~10 => 1
11~110 => 2
111~1110 => 3
1111~11110 => 4
'''

N = input()
L = len(N)

compare = '1'*(L-1) +'0'

if L == 1:
    print(1)
elif int(N) <= int(compare):
    print(L-1)
else:
    print(L)
