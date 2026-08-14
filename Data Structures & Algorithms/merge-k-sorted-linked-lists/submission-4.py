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

        # create dummy for return
        dummy = ListNode(-1)
        curr = dummy
        counter = itertools.count()
        minheap = []
        # dump everything into a minheap
        for i, head in enumerate(lists):
            curr = lists[i]
            while curr:
                heapq.heappush(minheap, (curr.val, next(counter), curr))
                curr = curr.next
        
         # create dummy for return
        dummy = ListNode(-1)
        curr = dummy
        while minheap:
            curr.next = heapq.heappop(minheap)[2]
            curr = curr.next
        if curr:
            curr.next = None
        
        
        return dummy.next
                
                

                


        