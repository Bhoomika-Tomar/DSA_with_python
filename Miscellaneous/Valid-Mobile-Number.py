class Solution:
    def check_valid (self, s):

        if s.startswith ("91"):
            s = s[2:]

        elif s.startswith ("0"):
            s = s[1:]

        
        if len(s) != 10:
            return False

        elif not s.isdigit():
            return False

        elif s[0] not in ["6" , "7", "8" , "9"]:
            return False

        else:
            return True

s = input ("Enter the mobile number")
sol = Solution()

if  sol.check_valid (s):
    print("Valid Number")

else:
    print ("Invalid number")