n=int(input())
m=list(map(int,input().split(' ')))
mi=min(m)
mx=max(m)
print(m.index(mi)+1,m.index(mx)+1)
