class Solution:
    
    def trimleadingzeros (self, head):
        while head and head.data == 0:
            head = head.next
            
        return head
        
    def length (self, head):
        count = 0
        while head != None:
            count = count + 1
            head = head.next
        return count
        
    def reverse (self, head):
        curr = head
        prev = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
            
    
    def addTwoLists(self, num1, num2):
        # code here
        
        #TRIM LEADING ZEROS
        num1 = self.trimleadingzeros (num1)
        num2 = self.trimleadingzeros (num2)
        
        #FINDING LENGTH OF EACH LINKED LIST
        len1 = self.length (num1)
        len2 = self.length (num2)
        
        if len1 < len2:
            return self.addTwoLists (num2, num1)
            
        #REVERSING EACH LINKED LIST
        num1 = self.reverse (num1)
        num2 = self.reverse (num2)
        
        carry = 0
        res = num1 
        
        while num2 != None or carry != 0:
            num1.data += carry
            
            if num2 != None :
                num1.data += num2.data
                num2 = num2.next
                
            carry = num1.data // 10
            num1.data = num1.data % 10
            
            if num1.next == None and carry != 0:
                num1.next = Node (0)
                
            num1 = num1.next
                
        return self.reverse(res)

