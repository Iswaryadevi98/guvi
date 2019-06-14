m,p=map(int,input().split())
l2=list(map(int,input().strip().split()))[:m]
for i in range(0,m):
  if(l2[i]==p):
    print("yes")
    break
  else:
    print("no")
