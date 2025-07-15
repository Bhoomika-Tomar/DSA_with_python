class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        
        #USING STACK

        max_area = 0
        stack = []           #to store indices
        heights.append(0)    #to flush stack at end

        for i, h in enumerate (heights):
            while stack and heights[stack[-1]] > h:

                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area

heights = list(map(int, input("Enter heights").split()))
sol = Solution()
print(sol.largestRectangleArea(heights))

