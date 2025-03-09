class Solution:
    def LCA(self, root, n1, n2):
        # your code here
        
        curr = root
        
        while curr != None:
            if curr.data > n1.data and curr.data > n2.data:
                curr = curr.left
                
            elif curr.data < n1.data and curr.data < n2.data:
                curr = curr.right
                
            else:
                return curr
    