m,a,n=input(),0,0
for i in m: 
	if(i.isalpha()):
		a=a+1
	elif(i.isnumeric()):
		n=n+1
if(n>0 and a>0): 
	print('Yes')
else: 
	print('No')
