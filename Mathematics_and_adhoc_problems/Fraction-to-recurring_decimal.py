class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return "0"

        result = []

        #Sign handling
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)

        #Integer part
        integer_part = numerator // denominator
        result.append (str(integer_part))
        remainder = numerator % denominator

        if remainder == 0:
            return ''.join(result)
            

        result.append('.')

        #Remainder part
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                start_index = remainder_map[remainder]
                result.insert (start_index,"(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            digit = remainder // denominator
            result.append(str(digit))
            remainder %= denominator

        return "".join(result)


numerator = int (input("Enter the numerator"))
denominator = int (input("Enter the denominator"))
sol = Solution()
print (sol.fractionToDecimal(numerator , denominator)) 

        