class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction(left). 
    def rotateArr(self,arr,d):
        n= len(arr)
        d = d%n  #for counter clockwise

        #d = n - (d%n) #for clockwise (right)

        self.reverse (arr, 0, d-1)
        self.reverse (arr, d, n-1)
        self.reverse (arr, 0, n-1)


    def reverse (self, arr, start, end):
        while start < end:

            arr[start],arr[end] = arr[end],arr[start]
            start = start + 1
            end = end - 1

    
arr = list(map(int, input("Enter array: ").split()))
d = int(input("Enter the no."))
sol = Solution()
sol.rotateArr(arr, d)
print ("Array after rotation",arr)

