def pic(m):
    a,b=0,1
    for i in range(0,m*m):
        c=(a+b)%m
        a=b
        b=c
        if a==0 and b==1:return (i+1)
    
def fib(m,n):
    rem=m%pic(n)
    
    a,b=0,1
    c=rem
    for i in range(1,rem):
        c=(a+b)%n
        a=b
        b=c
    
    return b%m
m,n=map(int,input().split())
print(fib(m,n))

