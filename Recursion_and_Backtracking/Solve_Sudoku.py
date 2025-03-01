
class Solution:
    
    
    def sudokusolver_rec (self, mat,i , j, rows, col, box):
        n = len(mat)
        
        #REACHED NTH COLUMN OF LAST ROW
        if i == n - 1 and j == n:
            return True
            
        #IF REACHED TO LAST COLUMN THEN MOVE TO NEXT ROW
        if j == n:
            i = i + 1
            j = 0
            
        #IF CELL IS ALREADY OCCUPIED THEN MOVE FORWARD
        if mat[i][j] != 0:
            return self.sudokusolver_rec (mat, i, j+1, rows, col, box)
            
        for num in range (1, n + 1):
            #IS IT SAFE TO PLACE AT CURRENT POSITION
            if self.isSafe (mat, i , j, num, rows, col, box):
                mat[i][j] = num
                
                #UPDATE MASKS FOR CORR. ROW , COL, BOX
                rows[i] |= (1<<num)
                col[j] |= (1<<num)
                box[(i//3)*3 + (j//3)] |= (1<<num)
                
                if self.sudokusolver_rec (mat, i ,j+1, rows, col,box):
                    return True
                    
                #UNMASK NO num IN CORR. ROW,COL,BOX
                mat[i][j] = 0
                rows[i] &= ~(1<<num)
                col[j] &= ~(1<<num)
                box[(i//3)*3 + (j//3)] &= ~(1<<num)
                
        return False
        
    def isSafe (self, mat, i, j, num, rows, col, box):
        
        if (rows[i]&(1<<num)) or (col[j]&(1<<num)) or (box[(i//3)*3 + (j//3)]&(1<<num)):
            return False
            
        return True
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        
        # Your code here
        n = len(mat)
        rows = [0] * n
        col = [0] * n
        box = [0] * n
        
        #SET BITS IN BITMASKS FOR VALUES
        for i in range (n):
            for j in range (n):
                if mat[i][j] != 0:
                    rows[i] |= (1<<mat[i][j])
                    col[j] |= (1<<mat[i][j])
                    box[(i//3)*3 + (j//3)] |= (1<<mat[i][j])
                    
        self.sudokusolver_rec (mat, 0 ,0 , rows, col, box)
