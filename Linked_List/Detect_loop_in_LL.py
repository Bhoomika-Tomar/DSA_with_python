class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        
        #USING FLOYD'S CYCLE DETECTION ALGO
        
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            
            #MOVING SLOW ONE STEP FORWARD
            slow = slow.next
            
            #MOVING FAST TWO STEP FORWARD
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False
            