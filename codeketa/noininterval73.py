o=int(input())
k,l=input().split()
k=int(k)
l=int(l)
for i in range(k,l):
  if(i==o):
   print("yes")
   break
else:
  print("no")

