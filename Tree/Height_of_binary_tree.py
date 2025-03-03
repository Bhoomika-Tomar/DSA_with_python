class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        
        #USING RECURSION
        
        if root == None:
            return -1
            
        leftHeight = self.height (root.left)
        rightHeight = self.height (root.right)
        
        return max(leftHeight,rightHeight) + 1
