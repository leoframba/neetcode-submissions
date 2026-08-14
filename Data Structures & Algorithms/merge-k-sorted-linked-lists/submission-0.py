# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        cur = dummy

        while True:
            minVal =  1001
            tar = -1
            for i, head in enumerate(lists):
                if head:
                    # chck if the value is smaller than cur
                    if head.val < minVal:
                        minVal = head.val
                        tar = i
                    
            
            print(tar)
            if tar == -1: break

            node = lists[tar]
            lists[tar] = node.next

            cur.next = node
            cur = cur.next

            
        
        return dummy.next
                
            
            


        
                
                
