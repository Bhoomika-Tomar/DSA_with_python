class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Pointer in nums1
        last = m + n - 1

        #Pointer in nums1 , nums2
        i = m - 1
        j = n -1

        #Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i = i - 1

            else:
                nums1[last] = nums2[j]
                j = j - 1

            last = last - 1


        #If any more elemnts are left in nums2
        while j >= 0:
            nums1[last] = nums2[j]
            j = j -1
            last = last - 1


