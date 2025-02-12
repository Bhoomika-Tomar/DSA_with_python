class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # code here
        n = len(mat)
        
        #REVERSING EACH ROW
        for row in mat:
            row.reverse()
            
        #Transposing the entire matrix
        for i in range (n):
            for j in range (i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j] 
            

