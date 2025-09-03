class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        m = len(boxGrid)
        n = len(boxGrid[0])

        for i in range (m):
            empty = n - 1

            for j in range (n-1 , -1, -1):
                if boxGrid[i][j] == '*':
                    empty = j-1

                elif  boxGrid[i][j] == '#':
                    boxGrid[i][j], boxGrid[i][empty] = '.' , '#'
                    empty = empty - 1

        return [[boxGrid[m-1-i][j] for i in range(m)] for j in range (n)]