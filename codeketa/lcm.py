import math
s,t=input().split()
s=int(s)
t=int(t)
ans=(math.gcd(s,t))
print((s*t)//ans)
