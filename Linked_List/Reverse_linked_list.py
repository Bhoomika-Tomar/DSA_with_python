
class Solution:
    def reverseList(self, head):
        # Code here
        
        curr = head
        prev = None
        
        while curr != None:
            next = curr.next
            curr.next = prev
            
            prev = curr
            curr = next
            
        head = prev
        
        return head

