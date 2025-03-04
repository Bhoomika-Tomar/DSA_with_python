class Solution:
    
    def buildTreeRec (self, l, h, preorder, mp, index):
        
        if l > h:
            return None
            
        value = preorder[index[0]]
        root = Node(value)
        index[0] += 1
        
        root.left = self.buildTreeRec (l, mp[value]-1, preorder,mp,index)
        root.right = self.buildTreeRec (mp[value]+1, h, preorder,mp,index)
        
        return root
    
    def buildTree(self, inorder, preorder):
        # code here
        
        index = [0]
        n = len(inorder)
        #DICTIONARY TO STORE KEY-VALUE PAIRS 
        #KEY-NODE , VALUEE-INDEX OF NODE IN INORDER
        mp = { }
        
        for i in range (n):
            mp[inorder[i]] = i
            
        root = self.buildTreeRec (0, n-1, preorder, mp, index)
        
        return root
