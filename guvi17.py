n=int(input("enter a no: "))
t=0
r=n
while(r>0):
    a=r%10
    t=t+a**3
    r=r//10
if(t==n):
    print("yes")
else:
    print("no")
