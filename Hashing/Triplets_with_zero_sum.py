
#REVISE AGAIN

class Solution:
    def findTriplets(self, arr: list[int]) -> list[list[int]]:
        resSet = set()
        mp = {}
        n = len(arr)

        # Store all pair sums with their indices
        for i in range(n):
            for j in range(i + 1, n):
                pair_sum = arr[i] + arr[j]
                if pair_sum not in mp:
                    mp[pair_sum] = []
                mp[pair_sum].append((i, j))

        # For each number, check if its negative is a pair sum
        for k in range(n):
            rem = -arr[k]
            if rem in mp:
                for i, j in mp[rem]:
                    if k != i and k != j:
                        triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                        resSet.add(triplet)

        # Convert set of tuples to list of lists
        return [list(t) for t in resSet]


arr = list(map(int, input("Enter array: ").split()))
sol = Solution()
print(sol.findTriplets(arr))