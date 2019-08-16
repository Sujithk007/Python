m=input()
if(len(m)%2!=0):
	l=len(m)//2+1
	print(m[0:l-1]+'*'+m[l:])
else:
	l=len(m)//2
	print(m[0:l-1]+'**'+m[l+1:])
