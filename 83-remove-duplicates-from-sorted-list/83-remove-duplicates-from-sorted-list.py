# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        next_node = head.next
        current = head
        while next_node:
            if current.val == next_node.val:
                current.next = next_node.next
                next_node = next_node.next
            else:
                current = next_node
                next_node = next_node.next
        return head