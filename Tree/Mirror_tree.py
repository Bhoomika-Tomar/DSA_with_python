class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        
        if root == None:
            return
        
        #USING RECURSION
        self.mirror (root.left)
        self.mirror (root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp