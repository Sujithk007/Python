m,n=map(int,input().split(' '))
m=m+1
for i in range(m,n):
	if i>1:
		for j in range(2,i):
			if(i%j==0):
				break
		else:
			print(i,end=' ')
