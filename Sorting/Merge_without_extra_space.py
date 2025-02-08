class Solution:
    def mergeArrays(self, a, b):
        # code here
        #USING SHELL SORT
        n = len(a)
        m = len(b)
        #Adding 1 to find round off i.e. ceil value
        gap = (n+m+1)//2
        
        while gap>0:
            i=0
            j=gap
            
            while j < n+m:
                
                #when both pointers are in array a
                if j < n and a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                #when i is array a and j is in array b
                elif i < n and j >= n and a[i] > b[j-n]:
                    a[i], b[j-n] = b[j-n], a[i]
                #when both pointers are in array b
                elif i >= n and b[i-n] > b[j-n]:
                    b[i-n], b[j-n] = b[j-n], b[i-n]
                    
                i = i+1
                j = j+1
                
            if gap == 1:
                break
                
            #Updating the gap
            gap = (gap+1)//2
                
        return a+b