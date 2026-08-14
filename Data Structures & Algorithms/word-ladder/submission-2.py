from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case
        if beginWord == endWord:
            return 1
        # define a function to see if two words are one char apart
        # we will use this to build an adj list between words
        def is_one_char_diff(s1, s2):
            diffs = sum(1 for a, b in zip(s1, s2) if a != b)
            return diffs <= 1
        
        # creat the adj dict
        #adj = {beginWord: [], word: [] for word in wordList }
        #edge case
        # if endWord not in adj:
        #     return 0
        if endWord in wordList:
            wordList.insert(0, endWord)
        else:
            return 0

        visited = set()
        
        q = deque([(beginWord, [beginWord])])
        while q:
            curr, path = q.popleft()
            visited.add(curr)

            if curr == endWord:
                return len(path)

            for word in wordList:
                if word not in visited and is_one_char_diff(curr, word): # if its within one char we can traverse to it
                   q.append((word, path + [word]))

        # # create adj list
        # def dfs(node, count) -> int:
        #     count += 1

        #     if node == endWord:
        #         return count

        #     visited.add(node)
        #     print(visited)
        #     print(count)

        #     for word in wordList:
        #         if word not in visited and is_one_char_diff(node, word): # if its within one char we can traverse to it
        #            result = dfs(word, count)
        #            if result != 0:
        #             return result
        #     return 0
            
             
        return 0


        