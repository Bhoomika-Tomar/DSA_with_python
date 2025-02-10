class Solution:

    def kthElement(self, a, b, k):
        #Code here
        n = len(a)
        m = len(b)
        
        #If array a has more elements then call kth function
        #in reverse order
        if n > m:
            return self.kthElement (b, a, k)
            
        #For out of bound
        if k < 1 and k > n+m:
            return -1
            
        #Using binary search for including elements in 1st
        #part from array a
        low = max(0, k-m)
        high = min(k, n)
        
        while low <= high:
            mid1 = (low + high)//2
            mid2 = k - mid1
            
            #Elements on left and right of partition of array a
            l1 = (mid1==0 and float('-inf') or a[mid1-1])
            r1 = (mid1 == n and float('inf') or a[mid1])
            
            #Elements on left and right of partition of array b
            l2 = (mid2==0 and float('-inf') or b[mid2-1])
            r2 = (mid2 == m and float('inf') or b[mid2])
            
            #If the partition is valid
            if l1 <= r2 and l2 <= r1:
                return max(l1,l2)
            
            #Check if we ned to take more elements from a[]    
            if l1 > r2:
                high = mid1 - 1
            #Check if we ned to take less elements from a[]   
            else:
                low = mid1 + 1
            
        return -1

