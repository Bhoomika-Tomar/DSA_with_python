class Solution:
    def countDistinct(self, arr, k):
        # Code here
        
        n = len(arr)
        res = []
        
        #Dictionary to store distinct elements from size k
        freq = defaultdict (int)
        
        #Storing the frequency of elements from first window
        for i in range (k):
            freq[arr[i]] = freq[arr[i]] + 1
            
        #Storing the count of distinct elements from first window
        res.append (len(freq))
        
        for i in range (k, n):
            freq[arr[i]] = freq[arr[i]] + 1
            freq[arr[i - k]] = freq[arr[i - k]] - 1
            
            if freq[arr[i - k]] == 0:
                del freq[arr[i - k]]
                
            res.append(len(freq))
            
        return res
