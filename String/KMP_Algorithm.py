#constructing longest proper suffix (lps)
def constructlps (pat,lps):
    m = len(pat)
    len_ = 0
    lps[0] = 0 
    
    i=1
    while i<m:
        if pat[i] == pat[len_]:
            len_=len_+ 1
            lps[i] = len_
            i=i+1
            
        else:
            if len_ != 0:
                len_ = lps [len_ - 1]
            else:
                lps[i] = 0
                i = i +1
class Solution:
    def search(self, pat, txt):
        # code here
        n= len(txt)
        m = len(pat)
        
        lps = [0]*m
        res = []
        
        constructlps (pat,lps)
        
        i,j = 0,0
        while i<n:
            if txt[i] == pat[j]:
                i=i+1
                j=j+1
            
                if j==m:
                    res.append(i-j)
                    j= lps[j-1]
            
            else:
                if j != 0:
                    j=lps[j-1]
                else:
                    i = i+1
                
        return res        
                
                    