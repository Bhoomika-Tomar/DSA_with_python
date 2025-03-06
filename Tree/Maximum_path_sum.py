
class Solution:
    
    def findMaxSumRec (self, root, res):
        if root == None:
            return 0
            
        left = max (0, self.findMaxSumRec (root.left, res))
        right = max (0, self.findMaxSumRec (root.right, res))
        
        res[0] = max(res[0], left+right+root.data)
        
        return max (left , right) + root.data 
        
    
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        
        res = [root.data]
        
        self.findMaxSumRec (root, res)
        
        return res[0]
