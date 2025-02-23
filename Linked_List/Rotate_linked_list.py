
class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        
        if k == 0 or head == None:
            return head
            
        n = 1
        curr = head
        
        while curr.next != None:
            n = n + 1
            curr = curr.next
        
        k = k % n
        
        if k == 0:
            return head
            
        curr.next = head
        curr = head
        
        for i in range (1, k):
            curr = curr.next
            
        head = curr.next
        curr.next = None
        
        return head
