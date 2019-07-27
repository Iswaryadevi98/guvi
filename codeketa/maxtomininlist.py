a=int(input())
l1=list(map(int,input().split()))[:a]
l1.sort()
l2=l1[::-1]
for i in l2:
  print(i,end='')
