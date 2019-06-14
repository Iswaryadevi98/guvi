f=input()
count=0
k=len(f)
for i in f:
  if((i=='1')|(i=='0')):
    count=count+1
if(count==k):
  print("yes")
else:
  print("no")

