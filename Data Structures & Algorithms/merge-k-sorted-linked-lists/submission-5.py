# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
import itertools

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #brute force find the min and append that to the new list

        # create dummy for res list
        dummy = ListNode(-1)
        curr = dummy

        # counter for comapare
        counter = itertools.count()
        # Add heads
        minheap = [(node.val, next(counter), node) for node in lists if node]
        heapq.heapify(minheap)

        # proccess heads while there are still nodes left
        while minheap:
            # grab the current min
            min_node = heapq.heappop(minheap)[2] # we only care about val 2
            next_node = min_node.next

            # append the next val in that list if there is one
            if next_node:
                heapq.heappush(minheap, (next_node.val, next(counter), next_node))
            
            # attach min to the res list
            curr.next = min_node
            curr = curr.next
            curr.next = None # cut ties from old list
        
        
        return dummy.next
                
                

                


        