class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # find a dupe within a certain window range

        # maintain a window using a dict

        window = {}
        init_window_len = min(k + 1, len(nums))
        # generate tehe init counts of the window
        for i in range(init_window_len):
            if nums[i] in window:
                window[nums[i]] += 1
            else:
                window[nums[i]] = 1
        
        # check for dupes
        def check_window_for_dupes():
            if any(True for value in window.values() if value >= 2):
                return True
            return False
        
        # init window check
        if check_window_for_dupes():
            return True

        left = 0
        for i in range(k + 1, len(nums)):
            # slide window
            
            # drop the left side from the map
            window[nums[left]] -= 1
            if window[nums[left]] == 0:
                window.pop(nums[left])
            left += 1
            
            # attempt to add right
            if nums[i] in window:
                return True # found a dupe
            else:
                window[nums[i]] = 1
        
        # we made it to the end without finding any dupes
        return False


        



        

        
        
        