k,l=input().split()
k=int(k)
l=int(l)
ans=k*l
for i in range(0,ans+1):
 if(i**2==ans):
   print("yes")
   break
else:
  print("no")
