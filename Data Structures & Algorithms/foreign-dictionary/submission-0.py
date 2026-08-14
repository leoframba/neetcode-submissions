from typing import List
from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # STEP 1: Initialize Data Structures
        # We must initialize an empty set and 0 in-degree for EVERY unique character
        # that appears anywhere in the list to handle isolated letters.
        adj = {c: set() for word in words for c in word}
        in_degree = {c: 0 for c in adj}
        
        # STEP 2: Build the Graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # The Invalid Prefix Trap: 
            # If w1 is longer than w2, but w1 starts with w2, the dictionary is invalid.
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            # Find the first differing character
            for j in range(min_len):
                if w1[j] != w2[j]:
                    parent_char = w1[j]
                    child_char = w2[j]
                    
                    # Only add the edge if we haven't seen this exact rule before.
                    # This prevents double-counting the in-degree!
                    if child_char not in adj[parent_char]:
                        adj[parent_char].add(child_char)
                        in_degree[child_char] += 1
                        
                    # CRITICAL: We only learn from the FIRST differing character.
                    # We must break the inner loop immediately.
                    break 
                    
        # STEP 3: Kahn's Algorithm (Topological Sort)
        # Start with all letters that have absolutely no prerequisites
        q = deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        
        while q:
            curr = q.popleft()
            res.append(curr)
            
            # Reduce the requirement count for all letters that depended on 'curr'
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
                    
        # STEP 4: Cycle Detection
        # If the result length doesn't match the number of unique characters, 
        # it means some letters were stuck in a cycle and never hit 0 in-degree.
        if len(res) == len(in_degree):
            return "".join(res)
        return ""