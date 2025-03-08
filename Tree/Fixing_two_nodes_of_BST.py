class Solution:
    
    #RECURSION FUNCTION FOR INORDER TRAVERSAL TO FIND OUT
    #SWAPPED NODES
    def correctBSTRec (self,root,first, middle, last, prev):
        if root == None:
            return
        
        #Recur for LST
        self.correctBSTRec (root.left, first, middle, last, prev)
        
        if prev[0] != None and root.data < prev[0].data:
            
            #If this is the first violation
            if first[0] == None:
                first[0] = prev[0]
                middle[0] = root
            
            #If this is the second violation    
            else:
                last[0] = root
                
        prev[0] = root
        
        #Recur for RST
        self.correctBSTRec (root.right, first, middle, last, prev)
    
    
    def correctBST(self, root):
         # your code here
        
        first, middle, last, prev = [None], [None], [None], [None]
    
        self.correctBSTRec (root,first, middle, last, prev)
    
        if first[0] != None and last[0] != None:
            first[0].data, last[0].data = last[0].data, first[0].data
            
        elif first[0] != None and middle[0] != None:
            first[0].data,middle[0].data = middle[0].data,first[0].data
    
            