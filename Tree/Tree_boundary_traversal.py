
class Solution:
    
    def isleaf (self, root):
        if root.left == None and root.right == None:
            return True
        else:
            return False
            
    def collectboundaryleft (self, root, res):
        if root == None:
            return
        
        if self.isleaf(root) == False:
            res.append(root.data)
            
        if root.left :
            self.collectboundaryleft (root.left, res)
        else:
            self.collectboundaryleft (root.right, res)
            
    def collectboundaryright (self, root, res):
        if root == None:
            return
            
        if root.right :
            self.collectboundaryright (root.right, res)
        else:
            self.collectboundaryright (root.left, res)
            
        if self.isleaf(root) == False:
            res.append(root.data)
            
    def collectleaves (self, root, res):
        if root == None:
            return
        
        if self.isleaf(root):
            res.append (root.data)
            
        else:
            self.collectleaves (root.left, res)
            self.collectleaves (root.right, res)
    
    def boundaryTraversal(self, root):
        # Code here
        
        res = []
        
        if root == None:
            return res
            
        if self.isleaf (root) == False:
            res.append (root.data)
            
        self.collectboundaryleft (root.left, res)
        self.collectleaves (root, res)
        self.collectboundaryright (root.right, res)
        
        return res

