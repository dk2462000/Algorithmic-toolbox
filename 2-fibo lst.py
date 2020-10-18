def fib(x):
    d=0
    a,b=0,1
    for i in range(0,x):
            c=(a+b)%10
            
            a=b
            b=c
    return a%10
        
    


        
        
m =int(input())
print(fib(m))

