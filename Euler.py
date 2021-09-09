a=0
b=2
N=10
alph=0.5
h=(b-a)/N
t=a
w=alph
ti=[0]
wi=[alph]
def g(t,y):
    return y-t**2+1

for i in range (1,N+1):
    w=w+h*g(t,w)
    wi.append(w)
    t=a+i*h
    print (w)
    ti.append(t)
