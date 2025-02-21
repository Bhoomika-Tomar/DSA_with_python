
class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        
        mp = { }
        res = 0
        prefix_sum = 0
        n = len(arr)
        
        for i in range (n):
            prefix_sum = prefix_sum + arr[i]
            
            if prefix_sum == k:
                res = i + 1
                
            elif (prefix_sum - k) in mp:
                res = max(res, i - mp[prefix_sum - k])
                
            if prefix_sum not in mp:
                mp[prefix_sum] = i
                
        return res
    
