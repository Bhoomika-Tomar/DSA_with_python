class Solution:
    def two_sum (self, arr:list[int], target:int) -> list[int]:
        
        #USING DICTIONARY TO STORE NO AS KEYS AND THEIR INDEXES AS VALUES OF KEYS
        arr_map = {}

        for i,num in enumerate(arr):
            #ENUMERATE IS USED FOR TRAVERSAL AND RETURNS THE INDEX WITH THE VALUE IN ARRAY

            complement = target - num
            if complement in arr_map:
                return [arr_map[complement] , i]

            arr_map[num] = i


#INPUT HANDLING
arr = list(map(int,input("Enter the array").split()))
target = int(input("Enter the target"))
sol = Solution()
print (sol.two_sum(arr, target))
