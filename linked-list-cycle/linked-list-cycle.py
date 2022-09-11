# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        while(head):
            head = head.next
            try:
                if head and head.visited:
                    return True
            except:
                head.visited = True
        return False
        