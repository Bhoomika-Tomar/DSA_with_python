class Solution:
    def maxPartitions(self , s):
        # code here
        
        n = len(s)
        
        last = [-1] * 26
        
        #Traversing in reverse order to find last occurence of each character
        for i in range (n-1, -1, -1):
            if last[ord(s[i]) - ord('a')] == -1:
                last[ord(s[i]) - ord('a')] = i 
        
        #Store no of partitions        
        count = 0
        #To track farthest last occurence seen
        a = -1
        
        for i in range (n):
            a = max(last[ord(s[i]) - ord('a')], a)
            
            if a == i:
                count += 
                
        return count
                


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends