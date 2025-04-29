class Solution:
    def activitySelection(self, start, finish):
        #code here
        
        n = len(start)
        
        ans = 0
        arr = []
        
        for i in range (n):
            arr.append((finish[i], start[i]))
            
        arr.sort()
        
        finishTime = 0
        
        for i in range (n):
            activity = arr[i]
            
            if activity[1] > finishTime:
                finishTime = activity[0]
                
                ans += 1
                
        return ans


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends