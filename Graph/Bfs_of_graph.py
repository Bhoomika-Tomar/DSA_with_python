#User function Template for python3

#USING QUEUE

from collections import deque

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        
        n = len(adj)
        res = []
        q = deque()
        visited = [False] * n
        
        q.append(0)
        visited[0] = True
        
        while q:
            i = q.popleft()
            res.append (i)
            
            for x in adj[i]:
                if visited[x] == False:
                    visited[x] = True
                    q.append (x)
                    
        return res
        


#{  
 # Driver Code Starts
import sys
from queue import Queue
from typing import List


#Position this line where user code will be pasted.
def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())  # Number of vertices
        adj = []  # Adjacency list

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.bfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends