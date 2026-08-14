# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.toNumber(l1)
        n2 = self.toNumber(l2)
        res = n1 + n2
        print(f"n1 = {n1}, n2 = {n2}, res = {res}")
        return self.toLinked(res)
    
    def toNumber(self, head: Optional[ListNode]) -> int:
        cur = head
        count = 0
        place = 0 
        while cur:
            val = cur.val
            count += val * (10 ** place)
            place += 1
            cur = cur.next
        
        return count
    
    def toLinked(self, value: int) -> Optional[ListNode]:
        if value == 0:
            return ListNode(0)

        dummy = ListNode(0)
        cur = dummy
        
        while value > 0:
            cut = value % 10
            value = int(value / 10)
            cur.next = ListNode(cut)
            cur = cur.next
        
        cur = dummy.next
        while cur:
            print(cur.val)
            cur = cur.next
        return dummy.next
            


        