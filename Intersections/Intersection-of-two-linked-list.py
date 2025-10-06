class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        currA = headA
        while currA:
            currB = headB
            while currB:
                if currA == currB:
                    return currA

                currB = currB.next

            currA = currA.next

        return None