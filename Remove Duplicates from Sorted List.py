# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = -1000
        return_head = ListNode(val=None, next=None)
        linked_list = return_head
        while head:
            if head.val != current:
                current = head.val
                linked_list.next = ListNode(val=current, next=None)
                linked_list = linked_list.next
            head = head.next
        return return_head.next