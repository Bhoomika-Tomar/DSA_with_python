class Solution:
    
    #PREORDER: TRAVERSAL IN FOLLOWING ORDER - ROOT,LST,RST 
    def preorder (self, root, arr):
        
        if root == None:
            arr.append (-1)
            return 
        
        arr.append (root.data)
        self.preorder (root.left, arr)
        self.preorder (root.right, arr)
    
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        
        #CONVERTING TREE TO ARRAY
        arr = []
        
        self.preorder (root, arr)
        return arr
    
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, arr):
        #code here
        
        #CONVERTING ARRAY TO TREE
        
        index = [0]
        
        return self.constructBT (arr, index, len(arr))
        
        
    def constructBT (self, arr, index, n):
        if index[0] >= n:
            return None
            
        if arr[index[0]] == -1:
            index[0] += 1
            return None
            
        root = Node(arr[index[0]])
        index[0] += 1
        
        root.left = self.constructBT (arr, index, n)
        root.right = self.constructBT (arr, index, n)
        
        return root
    
