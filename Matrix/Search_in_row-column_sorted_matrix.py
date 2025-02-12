class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		
		#Calculating no of rows and columns
		n = len(mat)
		m = len(mat[0])
		#Begin searching with element in 1st row and last
		#column
		i = 0
		j = m -1
		
		while i < n and j >= 0:
		   
		    #If k is greater than mat[i][j] then search in down
		    #direction i.e. column
		    if x > mat[i][j]:
		        i = i + 1
		        
		    #If k is less than mat[i][j] then search in left
		    #direction i.e. row
		    elif x < mat[i][j]:
		        j = j - 1
		    
		    #If k is found at mat[i][j]
		    else:
		        return True
			        
		return False
		    
