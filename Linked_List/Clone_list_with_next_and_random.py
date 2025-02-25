class Solution:
    def cloneLinkedList(self, head):
        # code here
        
        #COPYING NEW NODES B/W ORIGINAL NODES
        curr = head
        while curr != None:
            newNode = Node (curr.data)
            newNode.next = curr.next
            curr.next = newNode
            curr = curr.next.next
            
        #COPYING RANDOM POINTERS FROM ORIGINAL TO NEW LIST
        curr = head
        while curr != None:
            if curr.random != None:
                curr.next.random = curr.random.next
            curr = curr.next.next
                
        #REMOVING ORIGINAL LINKED LIST
        cloneHead = head.next
        curr = head
        cloneCurr = cloneHead
        
        while cloneCurr.next != None:
            curr.next = curr.next.next
            cloneCurr.next = cloneCurr.next.next
            
            curr = curr.next
            cloneCurr = cloneCurr.next
            
        curr.next = None
        cloneCurr.next = None
            
        return cloneHead
                
             