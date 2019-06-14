h=input()
d=0
for i in range(0,len(h)):
  if h[i].isalpha():
    d=d+1
    break
for i in range(0,len(h)):
  if h[i].isdigit():
    d=d+1
    break
if(d==2):
  print("Yes")
else:
  print("No")



  
