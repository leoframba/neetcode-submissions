# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # we need to get a pointer to the end
        end = head
        count = 1
        while end.next:
            count += 1
            end = end.next
        
        if count == 1:
            return
        
        # move to mid
        mid = count // 2
        curr = head
        prev = None
        for i in range(mid):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = None
        

        #curr is now at mid + 1
        # reverse
        prev = None
        # curr is already set
        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        
        #prev is the head of the end list
        end = prev
        # curr is head of our starting list
        curr = head

        # while end:
        #     print(end.val)
        #     end = end.next
        # print()
        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        while curr and end:
            # hold the next
            curr_next = curr.next

            # set current to end
            curr.next = end

            end_next = end.next
            if curr_next:
                end.next = curr_next
                end = end_next
            
            curr = curr_next
  
            

            
        



        