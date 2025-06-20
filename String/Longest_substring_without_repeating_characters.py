class Solution:
    def substring (self, s:str) -> int :

        #USING HASH SET AND SLIDING WINDOW
        left = 0
        max_length = 0
        char_set = set() 

        n = len(s)

        for right in range (n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left = left + 1

            char_set.add(s[right])
            max_length = max (max_length, right-left+1)

        return max_length

s = input ("Enter the string")
sol = Solution()
print (sol.substring(s))