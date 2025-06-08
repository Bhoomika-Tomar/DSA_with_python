def pallindrome (str):
    n = len(str)
    s1 = str
    s = ""

    for i in range (n-1, -1, -1):
        s = s + str[i]

    if s == s1:
        print ("Pallindrome")
    else:
        print ("Not a pallindrome")

str = input("Enter string")
pallindrome(str)
