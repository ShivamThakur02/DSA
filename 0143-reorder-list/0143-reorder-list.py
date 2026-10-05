# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
       Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        head2=slow.next
        slow.next=None
        prev=None
        curr=head2
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        temp1,temp2=head,prev
        while temp2:
            nxt_1=temp1.next
            nxt_2=temp2.next
            temp1.next=temp2
            temp2.next=nxt_1
            temp1=nxt_1
            temp2=nxt_2     
         
        
        