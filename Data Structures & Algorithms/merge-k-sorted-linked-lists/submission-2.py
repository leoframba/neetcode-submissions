# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #brute force find the min and append that to the new list

        dummy = ListNode(-1)
        curr = dummy
        while curr:    
            min_idx = -1

            # find the min val node
            for i, head in enumerate(lists):
                if head:
                    # The first valid node is always the min
                    if min_idx == -1 or head.val <= lists[min_idx].val:
                        # compare to find the min
                        min_idx = i
            
            # if we have found the min of this loop:
            if min_idx != -1:
                # Set the node in the res
                curr.next = ListNode(lists[min_idx].val)
                # Move the node to the next node as we've consumed it
                lists[min_idx] = lists[min_idx].next

            curr = curr.next
        
        return dummy.next
                
                

                


        