# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        if list1:
            while list1.next:
                l.append(list1.val)
                list1 = list1.next
            l.append(list1.val)
        
        if list2:
            while list2.next:
                l.append(list2.val)
                list2 = list2.next
            l.append(list2.val)
        
        if len(l) != 0:
            temp_list = []
            for i in sorted(l):
                temp_list.append(ListNode(val=i, next=None))
            
            for i in range(len(temp_list)-1):
                temp_list[i].next = temp_list[i+1]
            return temp_list[0]
        else:
            return None