fib=[0, 1]
n = input('n= ')
for i in range (2,n+1):
    fib.append(fib[i-1]+fib[i-2])
d = fib[n]
print (d)
