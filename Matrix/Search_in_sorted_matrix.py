class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 
    	
    	#Using binary search
    	#CREATING 1D ARRAY FROM 2D ARRAY
    	
    	#Counting no of rows and columns
    	n = len(mat)
    	m = len(mat[0])
    	low = 0
    	high = (n*m) - 1
    	
    	while low <= high:
    	    mid = low + (high - low) // 2
    	    #Finding row and column of element at index mid
    	    row = mid // m
    	    column = mid % m
    	    
    	    if mat[row][column] == x:
    	        return True
    	        
    	    if mat[row][column] < x:
    	        low = mid + 1
    	    else:
    	        high = mid - 1
    	        
    	return False    	        
    	
    	