g=input()
l=len(g)
s=['a','e','i','o','u']
for i in range(0,l):
  if g[i] in s:
    print("yes")
    break
  else:
    print("no")
