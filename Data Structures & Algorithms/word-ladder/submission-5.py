from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wildcard_map = {}
        for word in wordList + [beginWord]:
                for i in range(len(word)):
                        pattern = word[:i] + '*' + word[i+1:]
                        wildcard_map.setdefault(pattern, []).append(word)

        
        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            curr, count = q.popleft()

            if curr == endWord:
                  return count
            
            for i in range(len(curr)):
                  pattern = curr[:i] + '*' + curr[i+1:]
                  for e in wildcard_map[pattern]:
                        if e not in visited:
                              visited.add(e)
                              q.append((e, count + 1))
        
        return 0
            


        