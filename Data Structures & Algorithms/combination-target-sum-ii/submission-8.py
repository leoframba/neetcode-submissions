class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # no dupes

        # sort the candidates for early prune + remove any outliers
        candidates.sort()
        while candidates and candidates[-1] > target:
            candidates.pop()

        # result list
        res = set()

        # curr list to track one single list in memory
        combo = []
        # i = index in the canidates list | total - sum of curr combo 
        # we use combo param to avoid having to do sum(combo)
        def bt(start, total):
            # wall condition - 
            # valid target
            if total == target:
                res.add(tuple(combo))
                return
            
            # invalid - overshoot target or overshoot list bounds
            if total > target or start >= len(candidates):
                return # bad combo go back to backtrack
            
            # at any given index we can choose to take or skip the current val

            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    # if current value is invalid all remaining vals must also be
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                combo.append(candidates[i])
                bt(i + 1, total + candidates[i])

                combo.pop()


            return
        
        bt(0, 0)
        return [list(tup) for tup in res]
        
        
        