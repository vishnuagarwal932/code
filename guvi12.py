n=input("Enter a no : ")
try:
    val=int(n)
    if n== str(n)[: : -1]:
        print("yes")
    else:
        print("no")
except ValueError:
    print("Invalid")
    
