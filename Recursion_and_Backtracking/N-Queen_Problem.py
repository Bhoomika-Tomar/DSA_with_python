class Solution:
    
    def nQueenUtil (self,j, n, rows, diag1, diag2, board, res):
        
        #WHEN ALL QUEENS ARE PLACED
        if j > n:
            res.append (board[:])
            return
        
        for i in range (1, n + 1):
            if rows[i] == False and diag1[i-j+n] == False and diag2[i+j] == False:
                rows[i] =  diag1[i-j+n] = diag2[i+j] = True
                board.append (i)
                
                #USING RECURSION FUNCTION
                self.nQueenUtil (j + 1, n, rows, diag1, diag2, board, res)
                rows[i] =  diag1[i-j+n] = diag2[i+j] = False
                board.pop()
                    
                
            
    
    def nQueen(self, n):
        # code here
        
        rows = [False] * (n + 1)
        diag1 = [False] * (2 * n + 1)
        diag2 = [False] * (2 * n + 1)
        
        board = [ ]
        res = [ ]
        
        self.nQueenUtil (1, n, rows, diag1, diag2, board, res)
        
        return res
        