x=int(input())
y=int(input())
for n in range(x+1,y):
  if n>1:
   for i in range(2,n):
     if(n%i==0):
       break    
   else:
     print(n)
