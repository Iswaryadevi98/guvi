n=int(input())
ls=list(map(int,input().split()))[:n]
l1=[]
for x in range(0,n):
  if(x==ls[x]):
    l1.append(x)
if(l1==[]):
  print("-1")
else:
  for i in l1:
    print(i,end=' ')
