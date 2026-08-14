class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        part = nums
        buf = 0
        while len(part) > 1:
            mid = int(len(part) / 2)
            cur = part[mid]
            if cur == target:
                return mid + buf
            elif  cur > target:
                part = part[:mid]
            else:
                part = part[mid:]
                buf += mid
        if part[0] == target:
            return 0
        else:
            return -1
        