class Solution:
    def firstPallindrome(self, words:list[str]) -> str:

        for word in words:
            if self.isPallindrome (word):
                return word

        return ""


    def isPallindrome (self, word:str):
        left = 0
        right = len(word) - 1
        
        while left < right:
            if word[left] != word[right]:
                return False

            left = left + 1
            right = right - 1

        return True


words_input = input("Enter the words")
words = words_input.split()
sol = Solution()
print(sol.firstPallindrome(words))
