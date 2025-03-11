class Solution:
    
    def mergeTwo (self, head1, head2):
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
            
        if head1 != None :
            curr.next = head1
        if head2 != None:
            curr.next = head2
            
        return dummy.next
        
        
    
    def mergelistsRec (self, i, j, arr):
        
        #If only single list is left
        if i == j:
            return arr[i]
            
        mid = i + (j - i)//2
        
        head1 = self.mergelistsRec (i, mid, arr)
        head2 = self.mergelistsRec (mid+1, j, arr)
        
        head = self.mergeTwo (head1, head2)
        
        return head
    
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        
        if len(arr) == 0:
            return None
            
        return self.mergelistsRec (0, len(arr)-1, arr)

