class Solution:
    def hammingWeight(self, n: int) -> int:
        
        #Begin from LSB

        count = 0

        while n:
            count += n & 1
            n >>= 1

        return count


n = int(input ("Enter the number"))
sol = Solution()
print(sol.hammingWeight(n))
