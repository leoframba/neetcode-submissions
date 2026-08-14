# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # we need to get a pointer to the end
        # end = head
        # count = 1
        # while end.next:
        #     count += 1
        #     end = end.next
        
        # if count == 1:
        #     return
        
        # # move to mid
        # mid = count // 2
        # curr = head
        # prev = None
        # for i in range(mid):
        #     prev = curr
        #     curr = curr.next
        # if prev:
        #     prev.next = None
        # move to the mid with fast/slow
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow.next # mid + 1
        slow.next = None
        
        # reverse
        prev = None
        # curr is already set
        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        
        #prev is the head of the end list
        zag = prev
        # curr is head of our starting list
        zig = head

        # while end:
        #     print(end.val)
        #     end = end.next
        # print()
        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        while zig and zag:
            # hold the next
            next_zig = zig.next
            next_zag = zag.next

            # set current to end
            zig.next = zag
            zag.next = next_zig
            
            zig = next_zig
            zag = next_zag
  
            

            
        



        