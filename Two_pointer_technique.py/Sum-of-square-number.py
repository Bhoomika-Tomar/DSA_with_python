import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        #a^2 + b^2 = c

        left = 0
        right = int(math.isqrt(c))   #Largest possible value for b

        while left < right:
            value = left * left + right * right

            if value == c:
                return True

            elif value < c:
                left = left + 1

            else:
                right = right - 1

        return False

c = int (input("Enter the number"))
sol = Solution()
print(sol.judgeSquareSum(c))

