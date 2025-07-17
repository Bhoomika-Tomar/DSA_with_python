class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        #USING BIT MANIPULATION AND SUBTRACTION

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        #Checking for sign
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        if negative:
            quotient = -quotient

        return quotient


dividend = int(input("Enter value of dividend"))
divisor = int(input("Enter value of divisor"))
sol = Solution()
print (sol.divide(dividend, divisor)) 
