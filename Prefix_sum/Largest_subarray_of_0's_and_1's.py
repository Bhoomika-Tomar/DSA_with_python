class Solution:
    def maxLen(self, arr):
        # code here
        
        #USING HASHMAP AND PREFIX SUM
        
        n = len(arr)
        res = 0
        prefixsum = 0
        mp = { }
        
        for i in range (n):
            
            #if element is 0 add -1 to the prefix sum
            prefixsum += -1 if arr[i] == 0 else 1
            
            if prefixsum == 0:
                res = i + 1
                
            #if prefix sum is seen before then update result
            if prefixsum in mp:
                res = max (res, i - mp[prefixsum])
                
            else:
                mp[prefixsum] = i
                
        return res
