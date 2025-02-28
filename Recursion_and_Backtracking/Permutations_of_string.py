class Solution:
    
    #USING HASHMAP
    
    #RECURSIVE FUNCTION TO GENERATE PERMUTATIONS
    def genPermutations (self, n, curr, cnt, res):
        #IF LENGTH OF CURRENT PERMUTATION EQUALS LENGTH
        #OF INPUT STRING THEN APPEND IT TO RESULT
        if len(curr) == n:
            res.append (curr)
            return
        
        #ITERATE THROUGH EACH CHARACTER IN FREQUENCY MAP
        for c, count in cnt.items():
            
            if count == 0:
                continue
            
            #ADDING CHARACTER TO PERMUTATION
            cnt[c] -= 1
            
            #RECUR TO ADD ANOTHER CHARACTER TO PERMUTATION
            self.genPermutations (n, curr + c, cnt, res)
            
            #BACKTRACK: TO RESTORE COUNT
            cnt[c] += 1
            
    #FUNCTION TO GENERATE UNIQUE PERMUTATIONS
    def findPermutation(self, s):
        # Code here
        #LIST TO STORE RESULT
        res = []
        
        #FREQUENCY MAP TO COUNT FREQUENCY OF CHARACTERS
        cnt = { }
        
        for c in s:
            cnt[c] = cnt.get (c, 0) + 1
            
        self.genPermutations (len(s), "", cnt, res)
        return res
        
        