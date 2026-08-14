# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
              return None
        
        while len(lists) > 1:
            merged_lists = []
            #merge
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None 
                merged_lists.append(self.mergeLists(l1, l2))
                # if l2:
                #     merged_lists.append(self.mergeLists(l1, l2))
                # else:
                #     merged_lists.append(l1)
            lists = merged_lists
        
        return lists[0]

        

        
        return None
    
    def mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next                
            cur = cur.next
        
        cur.next = l1 if l1 else l2
        return dummy.next