def countandmerge (arr,l,m,r):
    #For left and right halves
    n1 = m-l+1
    n2 = r-m
    #Lists for left and right halves
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    
    #Initialize
    res = 0 
    i = 0
    j = 0
    k = l
    
    while i<n1 and j<n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j = j+1
            res = res + (n1-i)
        k = k+1
        
    #Merge remaining elements
    while i<n1:
        arr[k] = left[i]
        i=i+1
        k=k+1
    while j<n2:
        arr[k] = right[j]
        j=j+1
        k=k+1
        
    return res
    
def countInv (arr,l,r):
    res = 0
    if l<r:
        m = (l+r)//2
        
        #Counting inversions in left and right arrays
        res = res+countInv(arr,l,m)
        res = res+countInv(arr,m+1,r)
        
        #Counting inversions between left and right subarrays
        res =res + countandmerge(arr,l,m,r)
        
    return res


class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        return countInv (arr,0,len(arr)-1)
