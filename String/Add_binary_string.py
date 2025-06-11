class Solution:

    def trimLeadingZeros(self, s):
        firstOne = s.find('1')
        return s[firstOne:] if firstOne != -1 else "0"

    def addBinary(self, s1, s2):
        # Trim leading zeros
        s1 = self.trimLeadingZeros(s1)
        s2 = self.trimLeadingZeros(s2)

        n = len(s1)
        m = len(s2)

        if n < m:
            s1, s2 = s2, s1
            n, m = m, n

        j = m - 1
        carry = 0
        result = []

        # Traverse both strings from end
        for i in range(n - 1, -1, -1):
            bit1 = int(s1[i])
            bitSum = bit1 + carry

            if j >= 0:
                bit2 = int(s2[j])
                bitSum = bitSum + bit2
                j = j - 1

            bit = bitSum % 2
            carry = bitSum // 2

            result.append(str(bit))

        if carry > 0:
            result.append('1')

        # Reversing to provide result
        return ''.join(result[::-1])


# Input and output
s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

sol = Solution()
print("Result:", sol.addBinary(s1, s2))
