# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Starting from node start reverse up to M nodes and return the new head of the list
        def reverseMNodes(m: int, start: Optional[ListNode]) -> Optional[ListNode]:
            # Cant work with a null node
            if not start:
                return None 
            
            # [1, 2, 3]
            prev = start
            curr = start.next
        
            # check if we have a valid amount of nodes
            for i in range(m - 1):
                if curr == None:
                    return start
                curr = curr.next
            
            curr = start.next
            for i in range(m - 1):
                # hold next
                nextn = curr.next
                # reverse
                curr.next = prev
                # iterate
                prev = curr
                curr = nextn
            
            start.next = reverseMNodes(k, curr)
            return prev
        
        return reverseMNodes(k, head)




        