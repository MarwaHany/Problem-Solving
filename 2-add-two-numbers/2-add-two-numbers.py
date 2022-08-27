# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = sl = ListNode()
        remainder = 0
        while l1 and l2:
            res = l1.val + l2.val + remainder
            remainder = 0
            if res > 9:
                sl.val = res % 10
                remainder = 1
            else:
                sl.val = res
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                sl.next = ListNode()
                sl = sl.next
        if l1:
            while l1:
                res = l1.val + remainder
                remainder = 0
                if res > 9:
                    sl.val = res % 10
                    remainder = 1
                else:
                    sl.val = res
                l1 = l1.next
                if l1:
                    sl.next = ListNode()
                    sl = sl.next
        if l2:
            while l2:
                res = l2.val + remainder
                remainder = 0
                if res > 9:
                    sl.val = res % 10
                    remainder = 1
                else:
                    sl.val = res
                l2 = l2.next
                if l2:
                    sl.next = ListNode()
                    sl = sl.next
        if remainder:
            sl.next = ListNode()
            sl= sl.next
            sl.val = remainder
            sl.next = None
        else:
            sl.next = None
        return start
            
        