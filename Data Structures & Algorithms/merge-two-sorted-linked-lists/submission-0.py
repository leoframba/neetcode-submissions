# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #establish the head
        dummy = ListNode()
        tail = dummy

        c1 = list1
        c2 = list2

        while c1 and c2:
            if c1.val <= c2.val:
                tail.next = c1
                c1 = c1.next
                tail = tail.next
                
            else:
                tail.next = c2
                c2 = c2.next
                tail = tail.next
            
        while c1:
            tail.next = c1
            c1 = c1.next
            tail = tail.next

        while c2:
            tail.next = c2
            c2 = c2.next
            tail = tail.next

    
        return dummy.next
        
                
                    


        