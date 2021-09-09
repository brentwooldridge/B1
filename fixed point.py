p0=12
TOL=10e-01
N0=30
def f(x):
    return x**2-1


i=1
while i<=N0:
    p=f(p0)
    if abs(p-p0)<TOL:
        print (p)
    i=i+1
    p0=p
