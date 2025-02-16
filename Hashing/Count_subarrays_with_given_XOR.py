class Solution:
    def subarrayXor(self, arr, k):
        # code here
        
        #Using map to store prefix array with their corresponding
        #XOR value
        mp = { } 
        prefix_xor = 0
        res = 0
        
        for val in arr:
            prefix_xor = prefix_xor ^ val
            
            res = res + mp.get (prefix_xor ^ k, 0)
            
            if prefix_xor == k:
                res = res + 1
                
            #Storing xor value of subarray in map
            mp[prefix_xor] = mp.get (prefix_xor , 0) + 1
            
        return res
