import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # edge
        n = len(nums)
        if n <= 1:
            return n
        
        # for any given i in subseq i is the "best tail" for that lenght. ie the min tail
        subseq = []
        subseq.append(nums[0])
        
        for i in range(1, n):
            if nums[i] > subseq[-1]:
                subseq.append(nums[i])
            else:
                # find the min val to replace
                idx = bisect.bisect_left(subseq, nums[i])
                subseq[idx] = nums[i]
        
        return len(subseq)
                

        
        

        