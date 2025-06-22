class Solution:
    def containsDuplicate (self, arr: list[int]) -> bool :

        n = len(arr)
        set_ = set()

        for num in arr:
            if num in set_:
                return True

            set_.add(num) 

        return False


arr = list(map(int, input("Enter array: ").split()))
sol = Solution()
print(sol.containsDuplicate(arr))