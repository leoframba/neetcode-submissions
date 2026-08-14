class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        num_set = set(nums)

        longest = 1
        for e in nums:
            if (e - 1) not in num_set:
                target = e + 1
                cur = 1
                while target in num_set:
                    cur += 1
                    target += 1
                if cur > longest:
                    longest = cur

        return longest 


        # target_dict = {}
        # for e in nums:
        #     if e in target_dict:
        #         target_dict[e + 1] = target_dict[e] + 1
        #     else:
        #         target_dict[e + 1] = 1
        
        print(target_dict)
        return max(list(target_dict.values()))
        


        