class Solution:
    
    def findPredecessor (self, root):
        curr = root.left
        while curr.right != None and curr.right != root:
            curr = curr.right
            
        return curr
    
    def inOrder(self,root):
        # code here
        
        #USING MORRIS TRAVERSAL
        res = []
        curr = root
        
        while curr != None:
            if curr.left != None:
                predecessor = self.findPredecessor (curr)
                
                if predecessor.right != None:
                    predecessor.right = None
                    res.append (curr.data)
                    curr = curr.right
                    
                else:
                    predecessor.right = curr
                    curr = curr.left
                    
            else:
                res.append(curr.data)
                curr = curr.right
        
        return res
