# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        cur = head
        prev = None
        listLen = 0
        while cur:
            node = ListNode(cur.val, prev)
            prev = node
            cur  = cur.next
            listLen += 1
        
        

        dummy = ListNode()
        dummy.next = head
        tail = prev
        for i in range(0, listLen, 2):
            
            cur1 = head
            head = head.next

            cur2 = tail
            tail = tail.next

            cur1.next = cur2
            cur2.next = head
        
        
        cur = dummy.next
        for i in range(0, listLen - 1):
            cur = cur.next
        cur.next = None



            
            

            
           


        