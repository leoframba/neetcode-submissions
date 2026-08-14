# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #initial approach - iterate through the list in sections of k and reverse

        #we dont know the init size of the list but if we calc it we could create size // k pointers and have them iterate at differnt speeds

        # 1) find out where we need to start the reverse

        # 2) Define our reverse logic
        # G
        def revMNodes(m: int, start: Optional[ListNode]) -> Optional[ListNode]:
            if not start: return None

            # we start from start + 1
            prev = start
            curr = start.next 

            for i in range(m - 1):
                if not curr :
                    return None # we were unable to complete reversal of m nodes
                
                #save the next node for iter
                nextn = curr.next

                # reverse
                curr.next = prev

                # iterate
                prev = curr
                curr = nextn
            
            # at this point we have reversed the inner nodes and prev is the new head
            start.next = curr

            return prev
        
        # setup a dummy in case we need to move the head
        dummy = ListNode(-1)
        dummy.next = head
        
        # slow will always sit right before the next pot k
        slow = dummy
        fast = head

        count = 0
        while fast:
            
            # for every valid node
            count += 1

            # we have found k valid nodes we must reverse
            if count == k:
                # save the old_head
                old_head = slow.next # this val will be our new tail

                # we reverse and get the new head of the reversed list
                new_head = revMNodes(k, old_head)
                if not new_head:
                    return dummy.next

                # we link our prev list to the new reversed list
                slow.next = new_head # this should be the same val as fast
                # we move the slow pointer to the new tail which was the old head
                slow = old_head
                #reset count
                count = 0
                fast = slow.next
            else:
                # go to next node
                fast = fast.next
        
        return dummy.next
        
        
                


                    
                


        