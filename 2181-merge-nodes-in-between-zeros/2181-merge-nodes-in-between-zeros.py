# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res_node = ListNode()
        temp = res_node
        summ = 0
        head = head.next
        while(head):
            if not head.val:
                temp.val = summ
                if head.next:
                    temp.next = ListNode()
                    temp = temp.next
                    summ = 0
            else:
                summ += head.val
            head = head.next
        return res_node
                
        