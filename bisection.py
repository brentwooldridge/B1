a= 0
b=3
i=1
N0=5
TOL=10e-5
def f(x):
        return x**2-4*x+4
FA=f(a)
while i<N0:
    p=a+(b-a)/2
    FP=f(p)
    if FP==0 or (b-a)/2<TOL:
        print (p)
    i=i+1
    if FA*FP>0 or (b-a)/2<TOL:
        a=p
    else:
        b=p

