# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if head and head.next:
            next_node = head.next
            while(current and next_node):
                next_node.val, current.val = current.val, next_node.val
                current = next_node.next
                if current: 
                    next_node = next_node.next.next
        return head
            