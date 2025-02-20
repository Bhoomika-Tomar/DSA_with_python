
class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        
        res = 0
        n = len (s)
        
        #Initializing last index of all characters as -1
        lastindex = [-1] * 26
        start  = 0
        
        for end in range (n):
            #Finding last index of s[end]
            #and upadting start
            start = max (start, lastindex[ord(s[end]) - ord("a")] + 1)
            
            #Updating res
            res = max (res, end - start + 1) 
            
            #Updating lastindex
            lastindex [ord(s[end]) - ord("a")] = end
            
        return res
