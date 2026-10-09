# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head:
            return None
        if head and not head.next:
            return True
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        head2=slow.next
        slow.next=None
        curr=head2
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        while head and prev:
            if head.val!=prev.val:
                return False
                break
            head=head.next
            prev=prev.next
        return True
        