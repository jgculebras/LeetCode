# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1N = 0
        list2N = 0

        dummy = ListNode()
        retList = dummy

        list1Node = list1
        list2Node = list2

        while list1Node is not None and list2Node is not None:
            if list1Node.val <= list2Node.val:
                retList.next = list1Node
                list1Node = list1Node.next

            else:
                retList.next = list2Node
                list2Node = list2Node.next
            retList = retList.next

        if list1Node:
            retList.next = list1Node
        elif list2Node:
            retList.next = list2Node

        return dummy.next