class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        
        #Counting no of rows
        m = len(mat)
        #Counting no of columns
        n = len(mat[0])
        #List for storing result
        res = []
        #Initializing the boundaries
        top = 0
        right = n - 1
        bottom = m - 1
        left = 0
        
        while top <= bottom and left <= right:
            
            #Including top row elements from left to right
            for i in range (left,right + 1):
                res.append(mat[top][i])
            top = top + 1
            
            #Including last column elements from top to bottom
            for i in range (top, bottom + 1):
                res.append(mat[i][right])
            right = right - 1
            
            #Including bottom elements from left to right 
            #if exists
            if top <= bottom:
                for i in range (right,left-1,-1):
                    res.append(mat[bottom][i])
                bottom = bottom - 1
                
            #Including column elements from bottom to top
            #if exists
            if left <= right:
                for i in range (bottom,top-1,-1):
                    res.append(mat[i][left])
                left = left + 1
                
        return res
            
