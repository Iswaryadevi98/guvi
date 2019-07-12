a=input()
a=list(a)
res=""
for i in range(0,len(a)-1,2):
  t=a[i+1]
  a[i+1]=a[i]
  a[i]=t
print(res.join(a))
