def fib(x):
    a,b=0,1
    d=0
    if x==0:
        x=0
   
    for i in range((x+1)%60):
       
        
        a,b=b%10,(a+b)%10
    if(a==0):return 9
    else :return b-1   
    
m=int(input())
print(fib(m))

