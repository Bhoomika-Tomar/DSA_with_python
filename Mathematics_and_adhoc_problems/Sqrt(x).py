class Solution:
    def sqrt(self,  x:int) -> int :

        #USING BINARY SEARCH

        low = 1
        high = x//2

        while low <= high:
            mid = (low + high) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                low = mid + 1

            else:
                high = mid - 1

        return high    #high will be floor of sqrt


x = int (input("Enter the integer"))
sol = Solution()
print (sol.sqrt(x)) 
