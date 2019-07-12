g,h=map(int,input().split())
o=list(map(int,input().split()))
for j in range(0,h):
    o=[o[-1]]+o[:-1]
print(*o,end=' ')
