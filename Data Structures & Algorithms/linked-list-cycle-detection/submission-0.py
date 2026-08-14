# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ids = set()
        cur = head
        while cur:
            mId = id(cur)
            cur = cur.next
            print(mId)
            if mId in ids:
                return True
            else:
                ids.add(mId)
        
        return False
        


        