class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        
        #Set to store unique elements of a[] and b[]
        st = set()
        count = 0
        
        #Put all uniques elemnts of a[] in st
        for i in range (len(a)):
            st.add(a[i])
            
        #Put all uniques elemnts of b[] in st
        for i in range (len(b)):
            st.add(b[i])
            
        res = []
        #Store all elements of set in resultant array
        for it in st:
            count = count + 1
            res.append (it)
            
        return count
        
