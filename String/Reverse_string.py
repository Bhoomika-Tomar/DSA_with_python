def rev_string (str):
    n = len(str)
    s = ""

    for i in range (n-1, -1, -1):
        s = s + str[i]

    return s

str = input ("Enter string")
print (rev_string (str))