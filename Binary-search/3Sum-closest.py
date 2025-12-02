class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range (n-2):
            l = i+1
            r = n-1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target:
                    l += 1

                elif curr_sum > target:
                    r -= 1

                else:
                    return curr_sum

        return closest_sum
        
        