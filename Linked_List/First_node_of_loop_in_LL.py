class Solution:
    def findFirstNode(self, head):
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
                slow = head
                while slow != fast:
                    #MOVING SLOW AND FAST ONE STEP FORWARD
                    slow = slow.next
                    fast = fast.next
                
                return slow
        
        return None
