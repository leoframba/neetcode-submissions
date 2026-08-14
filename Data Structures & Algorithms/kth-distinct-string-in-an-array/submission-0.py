from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        res = [key for key, value in count.items() if value == 1]

        return res[k - 1] if 0 <= k - 1 < len(res) else ""
        