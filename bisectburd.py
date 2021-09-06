a = 1.0
b = 2.0
N0 = 15
TOL = 10e-4
i = 1
def f(x):
    return x**3+4*x**2-10        
FA = f(a)
while i < N0:
    p = a+(b-a)/2
    FP = f(p)
    if FP == 0 or (b-a)/2<TOL:
        print(p)
    i = i+1
    if FP*FA > 0 or (b-a)/2<TOL:
        a = p
    else:
        b = p    
 