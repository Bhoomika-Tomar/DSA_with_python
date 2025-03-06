class Solution:
    
    def sumKRec (self, root, k, res, mp, sum):
        if root == None:
            return 0
            
        sum = sum + root.data
        
        res[0] = res[0] + mp.get(sum - k, 0)
        
        if sum == k:
            res[0] = res[0] + 1
        
        mp[sum] = mp.get(sum, 0) + 1
        
        self.sumKRec (root.left, k , res, mp, sum)
        self.sumKRec (root.right, k , res, mp, sum)
        
        mp[sum] = mp[sum] - 1
        
    
    def sumK(self,root,k):
        # code here
        
        #USING PREFIX SUM AND DICTIONARY
        
        res = [0]
        mp = {}
        
        self.sumKRec (root, k, res, mp, 0)
        
        return res[0]
        