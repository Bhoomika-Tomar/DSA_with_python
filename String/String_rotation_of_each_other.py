#computing longest proper suffix
def computelps(pat):
    n = len(pat)
    lps = [0]*n
    len_ = 0
    lps[0] = 0
    
    i = 1
    while i < n:
        if pat[i] == pat[len_]:
            len_ = len_ +1
            lps[i] = len_
            i = i+1
        else:
            if len_ != 0:
                len_ = lps[len_ - 1]
            else:
                lps[i] = 0
                i = i+1
    return lps

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        txt = s1 + s1
        pat = s2
        
        n=len(txt)
        m=len(pat)
        
        lps = computelps(pat)
        i,j = 0,0
        
        while i<n:
            if txt[i] == pat[j]:
                i=i+1
                j=j+1
                
            if j==m:
                return True
                
            elif i<n and txt[i] != pat[j]:
                if j != 0:
                    j=lps[j-1]
                    
                
                else:
                    i = i+1
                    
        return False