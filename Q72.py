m=input()
m.lower()
s=['a','e','i','u','o']
for i in m:
	if(i in s): 
		print('yes')
		break
else: 
	print('no')
