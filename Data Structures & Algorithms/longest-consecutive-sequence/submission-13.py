class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        # conver nums to a set as we dont care a bout dupes
        numSet = set(nums)

        # iterate 0 -> n look for the start
        # we will define a start by asking if there is a num in our set -1 then the curr
        max_seq = 1
        seq = 1
        for num in nums:
            curr = num
            # if theres num -1 this is not a start
            if curr - 1 in numSet:
                continue
            else:
                #calc seq
                while curr + 1 in numSet: # look for valid seq
                    seq += 1
                    max_seq = max(max_seq, seq)
                    curr += 1
                seq = 1
            
        return max_seq



        