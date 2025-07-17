class Solution:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:

        m = len(matrix)
        n = len(matrix[0])

        prefix = [[0] * n for x in range (m)]
        all_values = []

        for i in range (m):
            for j in range (n):

                xor_value = matrix[i][j]

                if i > 0:
                    xor_value ^= prefix[i-1][j]

                if j > 0:
                    xor_value ^= prefix[i][j-1]

                if i > 0 and j > 0:
                    xor_value ^= prefix[i-1][j-1]

                prefix[i][j] = xor_value
                all_values.append(xor_value)

        all_values.sort(reverse=True)
        return all_values[k-1]



# ----------- INPUT HANDLING -------------
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print(f"Enter {rows * cols} matrix elements separated by space:")

flat_input = list(map(int, input().split()))
assert len(flat_input) == rows * cols, "Invalid number of elements!"

# Convert to 2D matrix
matrix = [flat_input[i * cols:(i + 1) * cols] for i in range(rows)]


k = int(input("Enter value of k"))
sol = Solution()
print (sol.kthLargestValue(matrix, k)) 
