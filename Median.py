m=list(map(int,input().split(' ')))
r=m[0]
m.remove(r)
m=sorted(m)
print(m[r//2])
