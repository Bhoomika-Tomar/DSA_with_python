class Solution:
    def longestStringChain(self, words):
        # Code here
        
        #Sorting words acc to their lengths
        words.sort (key = len)
        
        #Using dictionary to store max chain length for eac word
        dp = { }
        res = 1
        
        for w in words:
            #Initialize the length of each current word
            dp[w] = 1
            for i in range (len(w)):
                pred = w[ : i] + w[i+1:]
                
                if pred in dp:
                    dp[w] = max(dp[w], dp[pred] + 1)
                    
            res = max(res, dp[w])
            
        return res
