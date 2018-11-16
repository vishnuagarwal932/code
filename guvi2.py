n=input("enter a no.")
try:
    n=int(n)
    if(n>=0):
        if(n%2==0):
            print("even")
        else:
            print("odd")
    else:
        print("invalid")
except ValueError:
    print("invalid")
