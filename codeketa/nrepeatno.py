def R(x): 
    l= len(x) 
    r= [] 
    for i in range(l): 
        k = i + 1
        for j in range(k, l): 
            if x[i] == x[j] and x[i] not in r: 
                r.append(x[i]) 
    return r 
n=int(input())
l1 = list(map(int,input().split()))[:n]
l2=R(l1)
l2.sort()
print(l2) 
