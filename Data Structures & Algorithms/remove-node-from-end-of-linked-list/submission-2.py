# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # create dummy node 
        left = dummy
        right = head 

        # move the right pointer to be n away from the left pointer 
        while n > 0 and right:
            right = right.next
            n -= 1

        # move both the right and left pointer until right reaches end
        while right:
            left = left.next
            right = right.next 

        left.next = left.next.next 
        # left should now be 1 before the node we want to delete
        return dummy.next 
