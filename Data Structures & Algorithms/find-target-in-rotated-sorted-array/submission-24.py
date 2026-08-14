class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f = 0
        numsLen = len(nums)
        r = numsLen - 1

        while f < r:
            # get middle value rounding down
            m = (f + r) // 2
            
            # get values to compare
            rValue = nums[r]
            mValue = nums[m]
            
            # if we fidn the target
            if target == mValue:
                return m


            if mValue > rValue:
                f = m + 1
            else:
                r = m
            
            
        buffer = r
        print(f"f = {f}, r = {r}")
        f = 0
        r = numsLen

        

        while f <= r:
            print(f"f = {f}, r = {r}")
            m = (f + r) // 2
            print(m)
            mNorm = m + buffer
            if mNorm > numsLen - 1:
                mNorm = mNorm % numsLen
            
                
            print(f"mNorm = {mNorm}")
            mValue = nums[mNorm]
            
            if mValue == target:
                return mNorm
            
            if mValue > target:
                r = m - 1

            if mValue < target:
                f = m + 1
            
        return -1

        