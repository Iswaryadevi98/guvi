
def R(x): 
    l= len(x) 
    r= [] 
    for i in range(l): 
        for j in range(i+1, l): 
            if x[i] == x[j] and x[i] not in r: 
                r.append(x[i]) 
    return r 
n=int(input())
l1 = list(map(int,input().split()))[:n]
l2=R(l1)
if(l2==[]):
  print("unique")
else:
 l2.sort()
 for i in l2:
   print(i,end='')
