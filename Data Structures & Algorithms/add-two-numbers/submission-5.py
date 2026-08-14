# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # convert both lists to ints

        curr = l1
        pos = 0
        num1 = 0
        while curr:
            num1 += curr.val * (10 ** pos)
            pos += 1
            curr = curr.next
        
        curr = l2
        pos = 0
        num2 = 0
        while curr:
            num2 += curr.val * (10 ** pos)
            pos += 1
            curr = curr.next

        res = num1 + num2

        dummy = ListNode(0)
        curr = None
        if res > 0:
            curr = ListNode(res % 10)
            dummy.next = curr
            res = res // 10

        while res > 0:
            # get the next val
            remainder = res % 10
            res = res // 10

            # create new node and link back as we need to reverse 975 -> 5 -> 7 -> 9
            next_node = ListNode(remainder)
            curr.next = next_node
            
            #iterate
            curr = next_node


        return dummy.next if dummy.next else dummy            

        
        
        