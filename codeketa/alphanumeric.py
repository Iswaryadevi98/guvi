u=input()
v=[]
for i in u:
  if(i.isnumeric()):
    v.append(i)
print(*v,sep='')
