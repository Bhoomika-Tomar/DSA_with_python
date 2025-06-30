class Solution:
    def missing_positive (self, arr:list[int]) -> int:

        n = len(arr)

        #Placing all elements in correct index
        for i in range (n):
            while 1<= arr[i] <=n and arr[arr[i]-1] != arr[i]:
                correct_index = arr[i] - 1
                arr[i],arr[correct_index] = arr[correct_index] , arr[i]

            for i in range (n):
                if arr[i] != i+1:
                    return i + 1
                
        return n + 1
            

arr = list(map(int, input("Enter the array").split()))
sol = Solution()
print (sol.missing_positive(arr))

