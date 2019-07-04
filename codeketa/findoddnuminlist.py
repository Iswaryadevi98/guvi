g,h=input().split()
g=int(g)
h=int(h)
l1=list(map(int,input().split()))[:g]
for i in range(0,g):
  if((l1[i]%2==1)):
   if(i==h):
     print(l1[i])
    
