# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB
        while a or b:
            if a is None:
                a=headB
            elif b is None:
                b=headA
            if a is b:
                return a
            a=a.next
            b=b.next