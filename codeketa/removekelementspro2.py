from itertools import combinations
l,m=map(int,input().split())
p=len(str(l))
l1=list(combinations(str(l),p-m))
l1.sort()
print(*l1[0],sep='')
