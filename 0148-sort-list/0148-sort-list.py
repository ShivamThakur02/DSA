# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head and not head.next:
            return head
        if not head:
            return None
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        left=head
        right=slow.next
        slow.next=None

        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
        
    def merge(self,left,right):
        dummy=ListNode()
        curr=dummy
        while left and right:
            if left.val<right.val:
                curr.next=left
                left=left.next
            else:
                curr.next=right
                right=right.next
            curr=curr.next
        if left:
            curr.next=left
        else:
            curr.next=right
        return dummy.next

        