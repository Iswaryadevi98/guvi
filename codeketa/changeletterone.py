q=input()
q=q.split()
q1=q[0]
q2=q[1]
c=0
i=0
while(i<len(q1)  and c<2):
  if(q1[i]!=q2[i]):
    c+=1
  i+=1
if(c==1 or c==0):
  print("yes")
else:
  print("no")
