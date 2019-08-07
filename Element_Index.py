m=list(map(int,input().split(' ')))
n=m[0]
m.remove(m[0])
for i in range(0,n): print("%d %d"%(m[i],i))
