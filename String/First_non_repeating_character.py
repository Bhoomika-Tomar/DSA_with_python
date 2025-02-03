
class Solution:
   
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        max_char = 26 
        
        #creating an array and initializing with -1
        vis = [-1] * max_char
        
        #traversing the string s
        for i in range (len(s)):
            if vis[ord(s[i])-ord('a')] == -1:
                vis[ord(s[i])-ord('a')] = i
                
            #character is seen again
            else:
                vis[ord(s[i])-ord('a')] = -2
                
        idx = float('inf')
        for i in range (max_char):
            if vis[i]>= 0:
                idx = min(idx, vis[i])
        
        return '$' if idx == float('inf') else s[idx]       
    
    