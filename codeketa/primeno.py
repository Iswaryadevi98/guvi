s,t=map(int,input().split())
w=0
for i in range (s,t+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else: 
        w+=1
print(w )
