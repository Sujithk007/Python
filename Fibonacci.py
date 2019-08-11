m=int(input())
pre,nex=1,1
for i in range(0,m):
	if(i==0):
		print('1',end=' ')
	else:
		print(nex,end=' ')
		pre,nex=nex,(pre+nex)
