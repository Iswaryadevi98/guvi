o,p=input().split()
o=int()
p=int()
l2=list(map(int,input().strip().split()))[:o]
for i in range(0,o):
  if(l2[i]==p):
    print("yes")
    break
  else:
    print("no")
