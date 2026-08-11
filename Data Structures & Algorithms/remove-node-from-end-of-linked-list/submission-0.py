# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = head
        count = 0 

        while counter:
            count += 1 
            counter = counter.next 

        target = count - n
        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, dummy

        while target >= 0:
            prev = curr
            curr = curr.next
            target -= 1 

        prev.next = curr.next
        return dummy.next
        

        
