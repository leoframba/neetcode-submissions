class Solution:
    def jump(self, nums: List[int]) -> int:

        stack = [0]
        jumps = 0
        n = len(nums)
        furthest = curr = 0
        visited = set()
        while stack:
            while stack:
                curr = stack.pop()
                visited.add(curr)
                if curr >= n - 1:
                    return jumps
                if curr + nums[curr] >= n -1:
                    return jumps + 1
                furthest = max(furthest, curr + nums[curr])
            
            jumps += 1
            for i in range(curr + 1, furthest + 1):
                if i not in visited:
                    stack.append(i)
           
            
        
        return -1
            

            

            
            
        