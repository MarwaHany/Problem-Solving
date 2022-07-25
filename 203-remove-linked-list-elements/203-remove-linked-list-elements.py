# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        # assuming that head node value == val
        while(head and head.val == val):
            head = head.next
        if head and head.next:
            # initializations (pointers to the first and the second nodes)
            prev_node = head
            current_node = head.next
            while (current_node):
                if current_node.val == val:
                    prev_node.next = current_node.next
                    current_node = current_node.next
                else:
                    prev_node = current_node
                    current_node = current_node.next
        return head