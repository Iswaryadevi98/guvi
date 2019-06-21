s=input()
t=""
for a in s:
  if a not in t:
    t=t+a
if(s==t):
  print("Yes")
else:
  print("No")
