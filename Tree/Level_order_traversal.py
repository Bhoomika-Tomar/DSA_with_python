class Solution:
    
    from collections import deque
    
    def levelOrder(self, root):
        # Your code here
        
        if root == None:
            return []
        
        #USING QUEUE FOR THEE APPROACH OF FIFO    
        res = []
        q = deque()
        currLevel = 0
        
        q.append(root)
        
        while q :
            q_len = len(q)
            res.append ([])
            
            for i in range (q_len):
                node = q.popleft ()
                res[currLevel].append(node.data)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                    
            currLevel = currLevel + 1
            
        return res
