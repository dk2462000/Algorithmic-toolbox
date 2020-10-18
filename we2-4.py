def l1(n1,n2):
    
    if n1==0:
        return n2
    else:
        return l1(n2%n1,n1)

    
a,b=input().split()
a=int(a)
b=int(b)

if a<=b:
        a,b=a,b

    
print(int((a*b)/l1(a,b)))