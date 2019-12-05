m=int(input())
l=[2,3,5,7,11,1]
def prime(k):
    for i in l:
        if(k%i==0):
            return i

s=1
while(m!=1):
    t=prime(m)
    if(m%t==0):
        if(t%2==0):
            s=s*t
        m=m//t
print(s)
    
