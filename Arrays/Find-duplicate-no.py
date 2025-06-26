#USING FLOYD'S TORTOISE AND HARE ALGO
#CYCLE DETECTION ALGO


class Solution:
    def duplicate (self, arr:list[int]) -> int:

        #Find the intersection point
        slow = arr[0]
        fast = arr[0]

        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]

            if slow == fast:
                break

        #Finding the intersection point again
        slow = arr[0]
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]

        return slow

    
arr = list(map(int, input("Enter the array").split()))
sol = Solution()
print (sol.duplicate(arr))

