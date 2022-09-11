# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # traverse and convert unidirectional linked list to bidirectional linked list
        head.previous = None
        temp = head
        root = ListNode()
        while(temp):
            if not temp.next:
                root = temp
            prev = temp           
            temp = temp.next
            if temp:
                temp.previous = prev
        l = head
        while(head!=root):
            if head.val != root.val:
                return False
            else:
                head = head.next
                root = root.previous
        return True
            
            
            