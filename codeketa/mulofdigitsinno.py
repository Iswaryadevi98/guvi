o=int(input())
s=1
while(o>0):
  d=o%10
  s=s*d
  o=o//10
print(s)
