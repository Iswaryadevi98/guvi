o,p,q=input().split()
o=int(o)
p=int(p)
q=int(q)
w=0
for i in range(1,q+1):
  w=w+(o+(q-i)*p)
print(w)
