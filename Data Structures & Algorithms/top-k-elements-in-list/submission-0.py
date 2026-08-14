class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map[n] = 1 + map.get(n, 0)

        sorted_e = sorted(map.items(), key=lambda x: x[1], reverse=True)
        print(sorted_e)

        res = [item[0] for item in sorted_e[:k]]

        return res
        