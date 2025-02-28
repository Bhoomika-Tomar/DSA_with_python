class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        
        #WHEN POWER IS ZERO
        if e == 0:
            return 1
            
        #WHEN POWER IS NEGATIVE
        if e < 0:
            return 1 / self.power (b , -e)
            
        temp = self.power (b, e//2)
        
        #WHEN POWER IS EVEN
        if e % 2 == 0:
            return temp * temp
            
        #WHEN POWER IS ODD
        else:
            return temp * temp * b

