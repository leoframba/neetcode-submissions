class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        trip_set = set()
        for i in range(len(nums)):
             for k in range(i + 1, len(nums)):
                for j in range(k + 1, len(nums)):
                    if nums[i] + nums[k] + nums[j] == 0:
                        trip_set.add((nums[i], nums[k], nums[j]))

        
        for s in trip_set:
            ans.append(list(s))
        return ans




        
        # target_dict = {}
        # for i in range(len(nums)):
        #     for k in range(i + 1, len(nums)):
        #         target = 0 - (nums[i] + nums[k])

        #         if target in target_dict:
        #             tl = target_dict[target]
        #             unique = True
        #             for s in tl:
        #                 if nums[i] in s:
        #                     unique = False
        #             if unique:
        #                 tl.append(set({nums[i], nums[k]}))
        #         else:
        #             target_dict[target] = [set({nums[i], nums[k]})]
        
        # print(target_dict)
        
        # ans = []
        # for i in range(len(nums)):
        #     if nums[i] in target_dict:
        #         tl = target_dict[nums[i]]
        #         for k in tl:
        #             if len(k) == 1:
        #                 pop_res = k.pop()
        #                 ans.append([pop_res, pop_res, nums[i]])
        #             elif len(k) == 2:
        #                 ans.append([k.pop(), k.pop(), nums[i]])                    
        # return ans
        