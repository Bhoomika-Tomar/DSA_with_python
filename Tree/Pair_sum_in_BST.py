class Solution:
    
    def inorder_traversal (self, root, inorder):
        if root == None:
            return
        
        self.inorder_traversal (root.left, inorder)
        inorder.append (root.data)
        self.inorder_traversal (root.right, inorder)
    
    def findTarget(self, root, target): 
        # your code here.
        
        #USING INORDER TRAVERSAL AND TWO POINTER TECHNIQUE
        inorder = []
        
        self.inorder_traversal (root, inorder)
        
        n = len(inorder)
        left = 0
        right = n - 1
        
        while left < right:
            if inorder[left] + inorder[right] < target:
                left = left + 1
                
            elif inorder[left] + inorder[right] > target:
                right = right - 1
                
            else:
                return True
                
        return False
