# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if not head:
            return None
        dummy=ListNode()
        dummy.next=head
        prev,curr=dummy,head
        while curr:
            if curr.val==val:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        return dummy.next
            