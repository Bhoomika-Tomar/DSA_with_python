class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        #USING BACKTRACKING

        candidates.sort()
        res = []

        def backtrack ( start, path, total):
            if total == target:
                res.append(path[:])
                return

            if total > target:
                return

            for i in range (start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                backtrack (i+1, path + [candidates[i]], total + candidates[i])

        backtrack(0, [], 0)
        return res


candidates = list(map(int, input("Enter candidates: ").split()))
target = int(input("Enter the target"))
sol = Solution()
print(sol.combinationSum2(candidates, target))