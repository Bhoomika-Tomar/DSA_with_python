class Solution:
    def mul_strings(self, num1:str, num2:str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)
        result = [0] * (m+n)

        num1 = num1[ : : -1]
        num2 = num2[ : : -1]

        for i in range (m):
            for j in range (n):
                mul = int(num1[i]) * int(num2[j])
                result[i+j] += mul
                result[i+j+1] += result[i+j] // 10   #CARRY OVER
                result[i+j] %= 10      #CURRENT DIGIT

        #REMOVING LEADING ZEROS
        while result[-1] == 0:
            result.pop()

        return ''.join (map(str, result[::-1])) 

num1 = (input("Enter the string1"))
num2 = (input("Enter the string2"))
sol = Solution()
print(sol.mul_strings(num1, num2))
