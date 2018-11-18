n,k=map(int,input("enter a no: ").split())
for i in range(n+1,k):
    t=0
    r=i
    while(r>0):
        a=r%10
        t=t+a**3
        r=r//10
    if(t==i):
        print(i)
    
