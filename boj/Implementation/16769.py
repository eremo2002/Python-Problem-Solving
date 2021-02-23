c, m = list(), list()

for i in range(3):    
    a, b = map(int, input().split())

    c.append(a)
    m.append(b)



def pour(c1, m1, c2, m2):     
    if c2 == m2:    # c2 is full
        return c1, m1, c2, m2
    elif c2 > m2:   # c2 is not full
        remain = c2-m2
        
        if remain >= m1:
            m2 += m1
            m1 -= m1
        elif remain < m1:
            m2 += remain
            m1 -= remain
    
    return c1, m1, c2, m2




for i in range(100):

    if i%3 == 0: # 1 -> 2
        c[0], m[0], c[1], m[1] = pour(c[0], m[0], c[1], m[1])
    elif i%3 == 1: # 2 -> 3
        c[1], m[1], c[2], m[2] = pour(c[1], m[1], c[2], m[2])
    else: # 3 -> 1
        c[2], m[2], c[0], m[0] = pour(c[2], m[2], c[0], m[0])

for i in m:
    print(i)
