def check (arr, k, pagelimit):
    
    #Starting with 1st student
    count = 1
    pagesum = 0
    
    #If adding new book exceeds the page limit then 
    #assign the book to next student
    for pages in arr:
        if pagesum + pages > pagelimit:
            count = count + 1
            pagesum = pages
        else:
            pagesum = pagesum + pages
            
    #if books can be assigned to less than k students then it
    #can be assigned to k students as well
    return count <= k


class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        
        #If number of students are more than no of books
        
        if k > len(arr):
            return -1
            
        #Using binary search
        low = max(arr)
        high = sum(arr)
        res = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            #checking for minimizing the max no of pages
            if check(arr, k, mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
                    
        return res
                    
