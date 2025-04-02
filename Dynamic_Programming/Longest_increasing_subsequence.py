class Solution:
    def lis(self, arr):
        # code here
        
        #USING BINARY SEARCH
        
        n = len(arr)
        ans = []
        
        ans.append (arr[0])
        
        for i in range (1, n):
            if arr[i] > ans[-1]:
                ans.append(arr[i])
                
            else:
                low = 0
                high = len(ans) - 1
                
                while low < high:
                    mid = low + (high-low) // 2
                    
                    if ans[mid] < arr[i]:
                        low = mid + 1
                        
                    else:
                        high = mid
                        
                ans[low] = arr[i]
                
        return len(ans)
       