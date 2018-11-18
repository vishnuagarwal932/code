n=int(input("Enter a no : "))
if(n>1):
    for i in range(2,n//2):
        if(n%i==0):
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
