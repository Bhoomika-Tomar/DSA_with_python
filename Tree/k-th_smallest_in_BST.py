class Solution:
    
    def kthSmallestRec (self, root, k , count):
        if root == None:
            return -1
            
        left = self. kthSmallestRec (root.left, k, count)
        
        if left != -1:
            return left
            
        count[0] += 1
        
        if count[0] == k:
            return root.data
            
        right = self.kthSmallestRec (root.right, k, count)
        return right
        
    
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        
        count = [0]
        
        return self.kthSmallestRec (root, k, count)
        
