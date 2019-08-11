import math 
m=int(input())
def Lg2(x): 
    if(x == 0): 
        return false; 
    
    return (math.log10(x) / math.log10(2)); 
  
if(math.ceil(Lg2(m)) == math.floor(Lg2(m))): 
    print("yes"); 
else: 
    print("no"); 
