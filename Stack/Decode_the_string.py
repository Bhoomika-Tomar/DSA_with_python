class Solution:
    def decodedString(self, s):
        # code here
        
        stack = []
        
        for i in range (len(s)):
            if s[i] != ']':
                stack.append (s[i])
                
            else:
                temp = []
                
                while stack and stack[-1] != '[':
                    temp.append (stack.pop())
                
                temp.reverse()
                stack.pop()
                
                num = []
                while stack and stack[-1].isdigit():
                    num.insert (0, stack.pop())
                    
                number = int ("".join(num))
                repeat = "".join(temp) * number
                
                stack.extend (repeat)
                
        return "".join (stack)
