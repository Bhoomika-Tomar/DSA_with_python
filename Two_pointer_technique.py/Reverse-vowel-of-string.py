class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        vowel = set("aeiouAEIOU")
        left = 0
        right = n - 1
        
        while left <= right:
            if s[left] not in vowel:
                left = left + 1
            
            elif s[right] not in vowel:
                right = right - 1

            else:
                s[left], s[right] = s[right], s[left]
                left = left + 1
                right = right - 1

        return "".join (s)