# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        # Loop continues as long as there are nodes left OR a carry left over
        while l1 or l2 or carry:
            # Get values (use 0 if one list is shorter than the other)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate new digit and carry
            total = v1 + v2 + carry
            carry = total // 10
            val = total % 10
            
            # Add to new list
            curr.next = ListNode(val)
            
            # Update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next