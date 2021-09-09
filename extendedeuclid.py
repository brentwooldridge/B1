import math
a=1000
b=102

def extendedEuclid(a,b):
    if b==0:
        return (1,0,a)
    (xp,yp,d)=extendedEuclid(b,a%b)
    
    return (yp, xp-math.floor(a/b)*yp,d)
print (extendedEuclid(a,b))
