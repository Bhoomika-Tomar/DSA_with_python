class Solution:
    def findTriplets(self, arr):
        # Your code here
        
        #Set to handle duplicacies
        resSet = set()
        mp = {}
        n = len(arr)
        
        #Storing sum of pairs with their indices
        for i in range (n):
            for j in range(i + 1, n):
                sum = arr[i] + arr[j]
                if sum not in mp:
                    mp[sum] = []
                mp[sum].append((i,j))
                
        #Storing remaining values to find sum as zero
        for i in range(n):
            rem = -arr[i]
            if rem in mp:
                for p in mp[rem]:
                    #Ensuring no two indices have same value
                    if p[0] != i and p[1] != i:
                        curr = sorted ([i, p[0], p[1]])
                        resSet.add(tuple(curr))
                        
        return [list(triplet) for triplet in resSet]
                    
