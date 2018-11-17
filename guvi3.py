list=['a','e','i','o','u','A','E','I','O','U']
ch=str(input("Enter a character"))
if('a'<=ch<='z' or 'A'<=ch<='Z'):
    if(ch in list):
        print("vowel")
    else:
        print("consonant")
else:
    print("invalid")

