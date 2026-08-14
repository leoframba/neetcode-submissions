class Solution:
        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            result = []
            def backtrack(start, curr, sum):
                if sum == target:
                    result.append(list(curr))
                    return
                                                                                        
                if sum > target:
                    return
                                                                                                                                
                for i in range(start, len(candidates)):
                    # skip duplicate canidates - requires sorting the canidate list to have values near each other
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    curr.append(candidates[i])
                    backtrack(i + 1, curr, sum + candidates[i])
                    curr.pop()

            candidates.sort()                                                                                                                                                                      
            backtrack(0, [], 0)                                                                                                     
            return result