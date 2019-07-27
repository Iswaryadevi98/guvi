n=int(input())
ls=list(map(int,input().split()))[:n]
for x in range(0,n):
  if(x==ls[x]):
    print(x,end='')
