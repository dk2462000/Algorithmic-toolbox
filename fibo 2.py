def fib(x):
    d=0
    a,b=0,1
    for i in range(0,x):
            c=a+b
            
            a=b
            b=c
    return a
        
    


        
        
m =int(input())
print(fib(m))
