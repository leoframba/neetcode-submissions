# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # Get the next val
            next = curr.next
            # Reverse
            curr.next = prev
            #Iterate
            prev = curr
            curr = next
        
        # return prev as by the end of the loop curr will be none
        return prev
        