class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        count = 0
        
        # We loop as long as there are nodes to explore (curr) 
        # OR nodes waiting to be processed on the stack
        while curr or stack:
            # 1. Go as deep left as possible, caching parents on the stack
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. At this point, curr is None. Pop the leftmost node available.
            curr = stack.pop()
            
            # 3. Process the node
            count += 1
            if count == k:
                return curr.val
            
            # 4. We've processed this node and its left side. Now check its right side.
            curr = curr.right
            
        return -1