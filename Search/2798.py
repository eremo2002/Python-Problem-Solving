nm = list(map(int, input().split(' ')))
card = list(map(int, input().split(' ')))

result = 0

for i in range(0, len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            summation = card[i] + card[j] + card[k]
            if summation > result and summation <= nm[1]:
                result = summation


print(result)
