s = input()

tmp = ''

flag = False

for i in range(len(s)):
    if s[i] == '<':
        if flag == False:
            print(tmp[::-1], end='')
            tmp=''
            
        flag = True
        print(s[i], end='')
    elif s[i] == '>':        
        flag = False
        print(s[i], end='')
    elif s[i] == ' ':
        print(tmp[::-1], end=' ')
        tmp = ''
    else:
        if flag == True:
            print(s[i], end='')    
        else:
            tmp += s[i]

print(tmp[::-1])
