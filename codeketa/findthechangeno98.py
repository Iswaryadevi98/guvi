r=int(input())
ls=list(map(int,input().split()))
p=ls[0]
if r==len(ls):
  for i in range(1,len(ls)):
    if ls[i]>p:
      p=ls[i]
    else:
      print(i-1)
      break
