class Solution:
    
    def findMatch (self, mat, word, x, y, w_index):
        #x,y:current position in 2D matrix
        #w_index:index till which pattern is matched
        
        w_len = len(word)
        n = len(mat)
        m = len(mat[0])
        
        #PATTERN IS MATCHED
        if w_index == w_len:
            return True
            
        #OUT OF BOUNDARY
        if x<0 or y<0 or x>=n or y>=m:
            return False
            
        #IF GRID MATCHES WITH A LETTER WHILE RECURSION
        if mat[x][y] == word[w_index]:
            
            #MARKING THIS CELL AS VISITED
            temp = mat[x][y]
            mat[x][y] = '#'
            
            #FINDING SUBPATTERNS IN 4 DIRECTIONS
            res = (self.findMatch(mat,word,x-1,y,w_index+1) or self.findMatch(mat,word,x+1,y,w_index+1) or self.findMatch(mat,word,x,y-1,w_index+1) or self.findMatch(mat,word,x,y+1,w_index+1))
        
            #MARKING THIS CELL AS UNVISITED AGAIN
            mat[x][y] = temp
            return res
            
        return False
        
        
	def isWordExist(self, mat, word):
		#Code here
		
		wlen = len(word)
		#COUNTING NO OF ROWS
		n = len(mat)
		#COUNTING NO OF COLUMNS
		m = len(mat[0])
		
		#WHEN TOTAL CHARACTERS IN MATRIX ARE LESS THAN 
		#WORD LENGTH
		if wlen > n * m:
		    return False
		    
		#TRAVERSING THE GRID
		for i in range (n):
		    for j in range (m):
		        
		        #IF FIRST LETTER OF WORD MATCHES THEN RECUR
		        #AND CHECK
		        if mat[i][j] == word[0]:
		            if self.findMatch (mat,word,i,j,0):
		                return True
		return False
