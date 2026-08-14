class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        num_len = len(nums)

        
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            front = i + 1
            rear = num_len - 1

            while front < rear:
                curr = nums[i] + nums[front] + nums[rear]
                if curr == 0:
                    ans.append([nums[i], nums[front], nums[rear]])
                
                    while front < rear and nums[front] == nums[front + 1]:
                        front += 1
                    while front < rear and nums[rear] == nums[rear - 1]:
                        rear -= 1
                    
                    front += 1
                    rear -= 1
                
                if curr > 0:
                    rear -= 1
                elif curr < 0:
                    front += 1
            

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
        