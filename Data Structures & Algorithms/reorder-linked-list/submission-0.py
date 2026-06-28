# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        

        dummy = ListNode(0)
        dummy.next = head
        l1, l2 = head, prev
        while l2.next:
            tmp1 = l1.next
            l1.next = l2
            tmp2 = l2.next
            l2.next = tmp1
            l1, l2 = tmp1, tmp2
        
        return 

        




        