class Solution:
    def myPow(self, x: float, n: int) -> float:

        pow = x ** n

        return float(pow)


x =  float(input("Enter the integer"))
n = int (input("Enter the integer"))
sol = Solution()
print (sol.myPow(x, n))