T = int(input())

result = [0 for _ in range(T)]

for i in range(T): 
    N, C = int(input()), list(map(int, input().split()))

    circuit = 0

    # check odd & even
    for j in range(len(C)):
        if C[j]%2 == 1:
            C[j] += 1
    
    if C.count(C[0]) == len(C):
        result[i] = circuit
        continue
    else:
        # distribute candy        
        while True:       

            tmp_list = []

            for idx, v in enumerate(C):
                tmp_list.append(C[idx]//2)

            for idx, v in enumerate(C):
                C[idx] = C[idx]//2 + tmp_list[idx-1]
                        
            for j in range(len(C)):
                if C[j]%2 == 1:
                    C[j] += 1
            
            circuit += 1
                      
            if C.count(C[0]) == len(C):
                result[i] = circuit
                break
            
    
for i in result:
    print(i)
