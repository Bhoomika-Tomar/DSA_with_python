class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:

        stones.sort()
        n = len(stones)

        max_moves = max(
            stones[-1] - stones[1] + 1 - (n-1),
            stones[-2] - stones[0] + 1 - (n-1)
        )
        
        min_moves = n
        j = 0

        for i in range (n):
            while j < n and stones[j] - stones[i] + 1 <= n:
                j += 1

            already_inside = j - i

            if already_inside == n - 1 and stones[j-1] - stones[i] + 1 == n -1:
                min_moves = min(min_moves, 2)

            else:
                min_moves = min(min_moves, n- already_inside)

        return [min_moves, max_moves]
