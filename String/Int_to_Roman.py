class Solution:
    def int_to_roman (self, num:int) -> str:

        #USING TUPLE FOR CALCULATION IN DESCENDING ORDER
        val_to_roman = [
            (1000,'M'),
            (900,'CM'),
            (500,'D'),
            (400,'CD'),
            (100,'C'),
            (90,'XC'),
            (50,'L'),
            (40,'XL'),
            (10,'X'),
            (9,'IX'),
            (5,'V'),
            (4,'IV'),
            (1,'I')
        ]

        roman = ""

        for value, symbol in val_to_roman :
            while num >= value:
                roman = roman + symbol
                num = num - value

        return roman

num = int(input("Enter the number"))
sol = Solution()
print(sol.int_to_roman(num))
