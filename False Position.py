

p0=0
p1=4
TOL=10e-100
N0=500


i=2

def f(x):
    return x**3-2*x**2-5

q0=f(p0)
q1=f(p1)

while i<=N0:
    p=p1-q1*(p1-p0)/(q1-q0)
    if abs(p-p1)<TOL:
         print(p)
    i=i+1
    q=f(p)
    if q*q1<0:
        p0=p1
        q0=q1
        p1=p
        q1=q
