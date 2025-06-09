class Solution:
    def myAtoi(self, s):
        # Code here
        sign = 1
        res = 0
        idx = 0
        
        #Ignoring the whitespaces
        while idx<len(s) and s[idx] == ' ':
            idx = idx + 1
            
        #Storing sign
        if idx < len(s) and (s[idx] =='-' or s[idx]=='+'):
            if s[idx]=='-':
                sign = -1
            idx = idx + 1
        
        #constructing number digit by digit
        while idx<len(s) and '0'<=s[idx]<='9':
            res= 10*res + (ord(s[idx])-ord('0'))
            
            if res> (2**31 - 1):
                return sign * (2**31-1) if sign == 1 else -2**31
            idx = idx + 1
                
        return res*sign


s = input ("Enter sting")
sol = Solution()
print (sol.myAtoi(s))



