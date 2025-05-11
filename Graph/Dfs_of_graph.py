#User function Template for python3


#USING RECURSION
class Solution:
    
    def dfs_rec (self, i, visited, res, adj):
        
        visited[i] = True
        res.append(i)
        
        for x in adj[i]:
            if visited[x] == False:
                self. dfs_rec ( x, visited, res, adj)
        
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        
        n = len(adj)
        visited = [False] * n
        res = []
        
        self.dfs_rec (0, visited, res, adj)
        
        return res
        
        


#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())
        adj = []

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.dfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends