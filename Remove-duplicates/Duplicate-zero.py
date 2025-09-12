class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        

        #USING AN EXTRA LIST
        
        n = len(arr)
        result = []

        for num in arr:
            result.append(num)

            if num == 0:
                result.append(0)

        for i in range (n):
            arr[i] = result[i]