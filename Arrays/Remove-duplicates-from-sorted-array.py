class Solution:
    def remove_duplicates (self, arr:list[int]) -> int :

        n = len(arr)
        #FIRST UNIQUE ELEMENT
        count = 1
        j = 0

        for i in range (1 , n):
            if arr[i] != arr[j]:
                j = j + 1
                arr[j] = arr[i]
                count = count + 1

        print ("Unique array", arr[ : count])
        return count


arr = list(map(int,input("Enter the array").split()))
sol = Solution()
print (sol.remove_duplicates(arr))
