# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next

        if count <= 1:
            return None
        
        target = count - n
        if target == 0:
            return head.next

        cur = head
        for i in range(target - 1):
            cur = cur.next
               
        prev = cur
        cur = cur.next
        prev.next = cur.next

        return head
        
        
        

        