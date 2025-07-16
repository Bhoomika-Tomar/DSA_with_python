class Solution:
    def calculate(self, s: str) -> int:
        
        #USING STACK

        result = 0
        stack = []
        number = 0
        sign = 1

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)

            elif char in '+-':
                result += sign * number
                number = 0
                sign = 1 if char == '+' else -1

            elif char == '(':
                stack.append (result)
                stack.append (sign)
                result = 0
                sign = 1

            elif char == ')':
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()

        
        result += sign * number
        return result

s = input ("Enter the expression")
sol = Solution()
print(sol.calculate(s))

