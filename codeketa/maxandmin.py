g=int(input())
ls=list(map(int,input().strip().split()))[:g]
mx=max(ls)
mn=min(ls)
print(mn,mx)
