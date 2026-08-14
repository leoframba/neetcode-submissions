# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        c = head
        prev = None
        while c:
            # go to next before flipping link
            nxt = c.next
            c.next = prev

            # the current node becomest the prev
            prev = c

            c = nxt
        

        
        return prev
            
        