

class Solution:
    

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        #Importing defalutdict
        from collections import defaultdict
        
        #Using frequency as keys
        res = defaultdict (list)
         
        #accessing each string within array
        for s in arr:
            #Initializing freq of each character as 0
            count = [0] * 26
            #Accessing each character of string
            for ch in s:
                count [ord(ch) - ord("a")]  += 1
                
            res[tuple(count)].append(s)
            
        return list(res.values())

