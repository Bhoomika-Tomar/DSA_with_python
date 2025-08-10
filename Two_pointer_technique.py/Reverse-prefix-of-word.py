class Solution:
    def reversePrefix(word: str, ch: str) -> str:

        chars = list(word)
        end = word.find(ch)  #for index of ch
        left = 0
        right = end

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return ('').join(chars)
