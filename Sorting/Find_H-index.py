class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        n = len(citations)
        freq = [0] * (n+1)
        
        #counting frequency of citations
        for cit in citations:
            if cit >= n:
                freq[n] = freq[n] +1
            else:
                freq[cit] = freq[cit] + 1
        
        idx = n 
        #keeping track of count of papers having atleast idx citations
        s = freq[n]
        while s < idx:
            idx = idx - 1
            s = s+ freq[idx]
        
        #returning largest index
        return idx