class Solution:


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # invalid input check
        # empty list
        if not candidates:
            return []
        
        res = []

        # track 3 params
        # start = the start index for building our combo
        # curr = current combo
        # total = curr total
        def bt(start, curr, total):
            # define wall
            # valid combo
            if total == target:
                res.append(curr.copy())
                return
            # we have overshot target or len    
            if total > target or start >= len(candidates):
                return

            for i in range(start, len(candidates)):
                # skip repeats
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # try val
                curr.append(candidates[i])
                bt(i + 1, curr, total + candidates[i])
                
                #backtrack
                curr.pop()
        
        bt(0, [], 0)
        return res