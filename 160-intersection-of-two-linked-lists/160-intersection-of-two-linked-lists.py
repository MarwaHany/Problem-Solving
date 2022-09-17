# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while(headA or headB):
            try:
                if headB.visited:
                    return headB
            except:
                pass
            if headB:
                headB.visited = True
                headB = headB.next
            try:
                if headA.visited:
                    return headA
            except:
                pass
            if headA:
                headA.visited = True
                headA = headA.next
        return None