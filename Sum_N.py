L=list(map(int,input().split(' ')))
K,Sum=L[1],0
for i in range(2,K+2): Sum=Sum+L[i]
print(Sum)
