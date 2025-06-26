class Solution:
    def product (self, arr:list[int]) -> list[int]:

        #USING PREFIX AND SUFFIX PRODUCTS

        n = len(arr)
        answer = [1]*n

        #Left-pass:prefix product
        prefix = 1
        for i in range (n):
            answer[i] = prefix
            prefix = prefix * arr[i]

        #Right pass:suffix product
        suffix = 1
        for i in range (n-1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix = suffix * arr[i]

        return answer


arr = list(map(int, input("Enter the array").split()))
sol = Solution()
print (sol.product(arr))
            
