
#Using binary search
def search (arr, k):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high-low)//2
        
        if k == arr[mid]:
            return True
            
        if k < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return False


class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	# code here 
    	
    	#Calculating no of rows and columns
    	n = len(mat)
    	m = len(mat[0])
    	
    	#Using binary search on ith row
    	for i in range (n):
    	    if search (mat[i], x):
    	        return True
    	
    	return False
    	