r=list(input())
l=len(r)
if(l%2==0):
  r[int(l/2)]='*'
  r[int((l/2)-1)]='*'
else:
  r[int(l//2)]='*'
for i in range(0,l):
  print(r[i],end='')
