m,cnt=int(input()),0
for i in range(2,m+1):
	if(m%i==0):
		cnt=cnt+1
if(cnt>2):
	print('yes')
else:
	print('no')
