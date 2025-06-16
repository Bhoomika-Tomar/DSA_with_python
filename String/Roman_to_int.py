class Solution:
    def roman_to_int (self, s:str) -> int:

        #Using dictionary to store key-value pairs
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total = 0
        n = len(s)

        for i in range (n):
            if i + 1 < n and roman[s[i]] < roman[s[i+1]]:
                total = total - roman[s[i]]

            else:
                total = total + roman[s[i]]

        return total

s = input("Enter roman value")
sol= Solution()
print (sol.roman_to_int(s))