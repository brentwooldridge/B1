#for n in [1,2,3,4,5,26,27,28,29,30,31,32]:
n=32

def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n>1:
        return fib(n-1)+fib(n-2)
print (fib(n)) 

  
