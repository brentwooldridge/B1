a=2166
b=6099

def Euclid(a,b):
    if b==0:
        return a
    else:
        return Euclid(b, a%b)
print (Euclid(a,b))
