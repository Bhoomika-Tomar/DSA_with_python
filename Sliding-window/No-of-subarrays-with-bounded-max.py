class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count (max_bound:int) -> int:
            count = 0
            length = 0

            for num in nums:
                if num <= max_bound:
                    length += 1
                    count += length

                else:
                    length = 0

            return count

        return count(right) - count(left-1)
