k=input()
lp=list(k)
if(lp[0]=='(' and lp[-1]==')'):
  if(lp.count('(')==lp.count(')')):
    print("yes")
  else:
    print("no")
else:
  print("no")
