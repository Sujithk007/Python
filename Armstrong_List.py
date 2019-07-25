p,q=map(int,input().split(' '))
p=p+1
for m in range(p,q):
	sum,t=0,m
	while(t!=0):
		d= t%10
		sum+=d**3
		t //=10
	if(m == sum):
		print(m,end=' ')
