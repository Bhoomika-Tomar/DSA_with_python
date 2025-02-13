class Solution:
    def setMatrixZeroes(self, mat):
        
        #Counting no of rows and columns
        n = len(mat)
        m = len(mat[0])
        c0 = 1
        
        #Traversing the matrix and marking first cell of
        #each row and column
        for i in range (n):
            for j in range (m):
                if mat[i][j] == 0:
                    #Mark the ith row
                    mat[i][0] = 0
                    #Mark the jth column
                    if j == 0:
                        c0 = 0
                    else:
                        mat[0][j] = 0
                   
        #Traversing the matrix from 1,1 to n-1,m-1
        for i in range (1, n):
            for j in range (1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
                    
        #Mark the first row
        if mat[0][0] == 0:
            for j in range (m):
                mat[0][j] = 0
                
        #Mark the first column
        if c0 == 0:
            for i in range (n):
                mat[i][0] = 0
        
        return mat