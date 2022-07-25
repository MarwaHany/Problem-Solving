# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # initializations
        prev_node = None
        current_node = head
        while True:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            if not next_node:
                break
            current_node = next_node
        return current_node