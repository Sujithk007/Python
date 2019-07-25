m=int(input())
sum,t=0,m
while(t!=0):
   d= t%10
   sum+=d**3
   t //=10
if(m == sum):
   print('yes')
else:
   print('no')
