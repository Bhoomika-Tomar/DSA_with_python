class Solution:
    
    def findPredecessor (self, root):
        curr = root.left 
        while curr.right != None and curr.right != root:
            curr = curr.right
            
        return curr
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        
        #USING MORRIS TAVERSAL
        
        value = -1
        curr = root
        
        while curr != None:
            if curr.left != None:
                predecessor = self.findPredecessor (curr)
                
                if predecessor.right != None:
                    predecessor.right = None
                    
                    if curr.data <= value:
                        return False
                    
                    value = curr.data
                    curr = curr.right
                    
                else:
                    predecessor.right = curr
                    curr = curr.left
                    
            else:
                if curr.data <= value:
                    return False
                    
                value = curr.data
                curr = curr.right
                
        return True

