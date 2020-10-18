def l1(n1,n2):
    
    if n1==0:
        return n2
    else:
        return l1(n2%n1,n1)

m,n=map(int,input().split())
print(l1(m,n))