class Solution:
    
    def diameter_rec (self, root, res):
        
        if root == None:
            return 0
            
        #USING RECURSION    
        leftHeight = self.diameter_rec (root.left, res)
        rightHeight = self.diameter_rec (root.right, res)
        
        res[0] = max(res[0], leftHeight + rightHeight)
        
        return max(leftHeight, rightHeight) + 1
    
    def diameter(self, root):
        # Your code here
        
        res = [0]
        self.diameter_rec (root, res)
        
        return res[0]
        