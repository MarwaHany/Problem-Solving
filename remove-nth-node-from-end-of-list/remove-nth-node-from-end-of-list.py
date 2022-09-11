# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummynode = ListNode()
        dummynode.next = head
        l = dummynode
        r = dummynode
        for i in range(n+1):
            if r is not None:
                r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummynode.next
        

            
        
        
            
        