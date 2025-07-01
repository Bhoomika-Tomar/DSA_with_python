class Solution:
    def power (self, n:int)->bool:

        return n > 0 and (n & (n-1)) == 0 #bitwise and


n = int (input("Enter the integer"))
sol = Solution()
print (sol.power(n))