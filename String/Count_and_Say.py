class Solution:
    def count_and_say (self, n:int)->str :

        #Base case
        result = "1"

        for x in range (n-1):
            i = 0
            current = ""

            while i < len(result):
                count = 1
                while i+1 < len(result) and result[i] == result[i+1]:
                    count = count+1
                    i = i+1

                current = current + str(count) + result[i]
                i = i+1

            result = current
            

        return result

    
n = int(input("Enter the length"))
sol = Solution()
print(sol.count_and_say (n))
