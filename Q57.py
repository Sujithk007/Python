m=list(map(int,input().split(' ')))
n,k=m[0],m[1]
m.remove(n)
m.remove(k)
print(m.count(k))
