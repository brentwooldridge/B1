import math
x = 1
y = 3
def mult(x,y):
    if y==0:
        return 0
    z = mult(x,math.floor(y/2))
    if y%2==0:
        return 2*z
    else:
        return x+2*z
print(mult(x,y))