M=input()
M=M.lower()
l=['a','e','i','o','u']
if(M.isalpha()):
    for i in l:
    	if(i==M):
	    	print('Vowel')
	    	break
    else:
	    print('Consonant')
else:
    print('invalid')
