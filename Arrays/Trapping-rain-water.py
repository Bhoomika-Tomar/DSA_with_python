
#USING TWO POINTER TECHNIQUE

class Solution:
    def rain_water (self, arr:list[int]) -> int:

        n = len(arr)
        res = 0

        left = 1
        right = n-2

        lmax = arr[left-1]
        rmax = arr[right+1]

        while left <= right:

            if rmax <= lmax:
                res = res + max(0, rmax-arr[right])
                rmax = max(rmax, arr[right])
                right = right - 1

            else:
                res = res + max(0, lmax-arr[left])
                lmax = max(lmax, arr[left])
                left = left + 1

        return res  


arr = list(map(int, input("Enter the array").split()))
sol = Solution()
print (sol.rain_water(arr))