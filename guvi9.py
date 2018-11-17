n,k=map(int,input("enter the value of N and K : " ).split())
a=[]
sum=0
for i in range(1,n+1):
    t=int(input())
    a.append(t)
for i in range(k):
    sum=sum+a[i]
print(sum)
