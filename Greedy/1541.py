n = input()
n = n.split('-')

# remove '0005' -> 5
for i in range(len(n)):
    if '+' not in n[i]:
        n[i] = (int(n[i]))
    else:
        tmp = n[i].split('+')
        tmp_val = 0
        for j in tmp:
            tmp_val += int(j)
        
        n[i] = tmp_val



# calcuate sum
res = 0
for i in range(len(n)):
    if i == 0:
        res += n[i]
    else:
        res += -(n[i])

print(res)
