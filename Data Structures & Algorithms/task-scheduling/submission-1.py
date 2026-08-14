from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        
        # 1. Find the highest frequency
        max_freq = max(counts.values())
        
        # 2. Count how many unique tasks share that highest frequency
        max_freq_count = sum(1 for v in counts.values() if v == max_freq)
        
        # 3. Apply the greedy formula
        intervals = (max_freq - 1) * (n + 1) + max_freq_count
        
        # 4. Return the max of the formula or the raw number of tasks
        return max(len(tasks), intervals)