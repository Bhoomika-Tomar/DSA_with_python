import heapq

class Solution:
    
    def jobSequencing(self, deadline, profit):
        # code here
        n = len(deadline)
        
        ans = [0,0]
        jobs = [[deadline[i], profit[i]] for i in range (n)]
        jobs.sort()
        
        pq = []
        
        for job in jobs:
            if job[0] > len(pq):
                heapq.heappush(pq, job[1])
                
            elif pq and pq[0] < job[1]:
                heapq.heappop (pq)
                heapq.heappush (pq, job[1])
                
        while pq:
            ans[1] += heapq.heappop (pq)
            ans[0] += 1
            
        return ans
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        deadline = list(map(int, input().strip().split()))
        profit = list(map(int, input().strip().split()))

        obj = Solution()
        ans = obj.jobSequencing(deadline, profit)
        print(ans[0], ans[1])
        print("~")
# } Driver Code Ends