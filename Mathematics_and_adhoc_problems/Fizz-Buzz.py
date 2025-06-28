class Solution:
    def fizz_buzz (self, n:int) -> list[str]:

        res = []

        for i in range (1, n+1):
            if i%3 == 0 and i%5 == 0:
                res.append("FizzBuzz")

            elif i%3 == 0:
                res.append("Fizz")

            elif i%5 == 0:
                res.append( "Buzz")

            else:
                res.append(str(i))

        return res

n = int (input("Enter the integer"))
sol = Solution()
print (sol.fizz_buzz(n))
