
class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        
        
        #hashmap to store character frequencies
        charCount = {}
        
        #counting frequencies of character in s1
        for ch in s1:
            charCount[ch] = charCount.get(ch,0) + 1
            
        #counting frequencies of character in  s2
        for ch in s2:
            charCount[ch] = charCount.get(ch,0) - 1
            
        #calculating the value of each character
        for value in charCount.values():
            if value != 0:
                return False
        
        return True
        