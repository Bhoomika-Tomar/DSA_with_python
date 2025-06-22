
class Solution:
    def pushZerosToEnd(self, arr: list[int]) -> None:
        count = 0  # position to place the next non-zero element

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1


arr = list(map(int, input("Enter array: ").split()))
sol = Solution()
sol.pushZerosToEnd(arr)
print("Array after pushing zeros to end:", arr)