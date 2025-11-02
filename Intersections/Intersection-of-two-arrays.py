class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        n = len(nums1)
        m = len(nums2)

        for i in range (n):
            for j in range (m):
                if nums1[i] == nums2[j]:
                        result.append(nums1[i])
                        break

        return list(set(result)
