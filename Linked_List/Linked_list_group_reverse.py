class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        
        curr = head
        newHead = None
        tail = None
        
        while curr != None:
            groupHead = curr
            prev = None
            count = 0
            
            while curr != None and count < k:
                next = curr.next
                curr.next = prev
                
                prev = curr
                curr = next
                count = count + 1
                
            if newHead == None:
                newHead = prev
                
            if tail != None:
                tail.next = prev
                
            tail = groupHead
            
        return newHead
