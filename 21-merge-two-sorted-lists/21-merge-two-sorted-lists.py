# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import deepcopy
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        linked_list = []
        previous_node_index = 0
        if not bool(list1) and not bool(list2):
            return list1
        else:
            temp_node = ListNode()
            while list1 and list2:
                if list1.val <= list2.val:
                    temp_node.val = list1.val
                    linked_list.append(deepcopy(temp_node))
                    list1 = list1.next
                else:
                    temp_node.val = list2.val
                    linked_list.append(deepcopy(temp_node))
                    list2 = list2.next
                print("temp_node", temp_node.val)
                temp_node.next = None
            while list1:
                temp_node.val = list1.val
                linked_list.append(deepcopy(temp_node))
                list1 = list1.next
                temp_node.next = None
            while list2:
                temp_node.val = list2.val
                linked_list.append(deepcopy(temp_node))
                list2 = list2.next
                temp_node.next = None
        # link nodes to form the linked list
        for i in range(0,len(linked_list)-1):
            linked_list[i].next = linked_list[i+1]
        return linked_list[0]
        