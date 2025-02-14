class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        
        #Put all elements of array a in set
        a_set = set(a)
        res = []
        
        for elem in b:
            if elem in a_set and elem not in res:
                res.append (elem)
                a_set.remove (elem) #To avoid duplicacies
                
        return res

