class Solution:

    # we need place markers for where to split
    def encode(self, strs: List[str]) -> str:
        
        return "".join(f"{len(s)}#{s}" for s in strs)
        

    def decode(self, s: str) -> List[str]:
        start = 0
        res = []
        print(s)
        n = len(s)
        while start < n: 
            # get len of slice
            end = start + 1
            while s[end] != '#':
                end += 1
            wlen = int(s[start: end])
            start = end + 1
            end = start + wlen
            res.append(s[start:end])
            start = end

        return res
