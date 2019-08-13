m=eval(input())
for i in range(2,m):
	if(m%i==0):
		print('no')
		break
else: print('yes')
