# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        size = 0

        # get size of the array so we now where the nth node is relevant to the front
        while curr:
            size += 1
            curr = curr.next

        # edge case
        if size < n or n < 1:
            return None # this idx doesnt exist -- takes care of empty
        
        idx_from_front = size - n

        curr = head
        prev = None
        while curr and idx_from_front > 0:
            idx_from_front -= 1
            prev = curr
            curr = curr.next
        
        # At this point curr = the node to remove
        if not prev: # case where we are removing head
            return head.next
        elif curr:    
            prev.next = curr.next
        
        return head
            
        