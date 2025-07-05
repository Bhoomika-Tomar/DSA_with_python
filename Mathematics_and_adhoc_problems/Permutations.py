class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        #USING BACKTRACKING

        result = []

        self.backtrack (nums, [], result)
        return result

    def backtrack (self, nums, path, result):

        if not nums:    #no more elements to permute
            result.append(path)
            return 

        for i in range (len(nums)):
            self.backtrack (nums[:i]+nums[i+1:], path+[nums[i]], result)

nums= list(map(int ,(input("Enter the list")).split()))
sol = Solution()
print (sol.permute(nums)) 
