h1,m1,h2,m2=map(int,input().split(' '))
t1,t2=h1*60+m1,h2*60+m2
if(t1>t2): r=t1-t2
else: r=t2-t1
print("%d %d"%(r//60,r%60))
