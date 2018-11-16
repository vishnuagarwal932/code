n=input("enter a no.")
try:
    n=int(n)
    if(n%2==0):
        print("even")
    else:
        print("odd")
except ValueError:
    print("invalid")
