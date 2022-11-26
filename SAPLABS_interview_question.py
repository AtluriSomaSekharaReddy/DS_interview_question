'''
find the sum of the given array(list) based on the level of the level of the list in the given nested list
EXAMPLE:[5,2,[7,-1],3,[6,[-13,8],4]] is calculated  as :
 5+2+ (2*(7-1)) +3+ (2*(6+(3*(-13+8))+4))
'''
arr=[5,2,[7,-1],3,[6,[-13,8],4]]
def check(l,c):
    s=0
    for i in l:
        if(type(i)==list):
            s=s+c*check(i,c+1)
        else:
            s=s+c*i 
    return s 
s=0
for i in arr:
    if(type(i)==int):
        s=s+i 
    else:
        s=s+check(i,2) 
print(s)
