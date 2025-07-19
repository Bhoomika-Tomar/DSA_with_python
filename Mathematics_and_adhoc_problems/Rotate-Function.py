class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        
        n = len(nums)
        total = sum(nums)

        #Calculating F(0)
        F = sum(i * n for i , n in enumerate(nums))
        max_value = F

        #Calculating F(k) by formula 
        for k in range (1, n):
            F = F + total - n * nums[-k]
            max_value = max(max_value, F)

        return max_value
        
        
nums = list(map(int, input("ENTER ARRAY").split()))
sol = Solution()
print (sol.maxRotateFunction(nums)) 
