m,s=list(map(int,input().split(' '))),0
n=m[0]
m.remove(n)
for i in m: s=s+i
print(s//n)
