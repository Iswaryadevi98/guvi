v,w=map(str,input().split())
if(len(v)!=len(w)):
  print("no")
else:
  d=[v.count(i) for i in v]
  e=[w.count(i) for i in w]
if(d==e):
  print("yes")
else:
  print("no")
