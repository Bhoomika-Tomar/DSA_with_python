# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        values = []
        curr = head

        while curr:
            values.append (curr.val)
            curr = curr.next

        values.sort()

        dummy = ListNode(0)
        curr = dummy

        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.nex