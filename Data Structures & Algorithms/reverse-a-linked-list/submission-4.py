# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head.val:
        #     return ListNode()
        
        c = head
        prev = None
        while c:
            node = ListNode(c.val, prev)
            prev = node
            c = c.next
        

        
        return prev
            
        