p,q=input().split()
p=int(p)
q=int(q)
la=list(map(int,input().split()))[:p]
la.sort()
print(la[q-1])
