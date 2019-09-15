n=int(input())
m=list(map(int,input().split(' ')))
mi,mx=min(m),max(m)
print(m.index(mi)+1,m.index(mx)+1)
