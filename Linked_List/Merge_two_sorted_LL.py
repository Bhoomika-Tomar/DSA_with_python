
class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        
        #Creating a dummy node with data as -1
        dummy = Node (-1)
        curr = dummy
        
        while head1 != None and head2 != None:
            if head1.data <= head2.data:
                curr.next = head1
                head1 = head1.next
                
            else:
                curr.next = head2
                head2 = head2.next
                
            curr = curr.next
                
        if head1 != None:
            curr.next = head1
            
        if head2 != None:
            curr.next = head2
            
        return dummy.next
            
