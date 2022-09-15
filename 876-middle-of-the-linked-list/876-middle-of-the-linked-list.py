# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_map = dict()
        # hash_map[1] = head
        count = 0
        while(head):
            count += 1
            hash_map[count] = head
            head = head.next
        
        return hash_map[count//2+1]
        