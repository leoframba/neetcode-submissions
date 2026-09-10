class Solution:
    DELI = '#'
    # create a deli
    def encode(self, strs: List[str]) -> str:
        encoded = "".join(
            f"{len(s)}{self.DELI}{s}"
            for s in strs 
        )
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            r = i + 1
            while s[r] != self.DELI:
                r += 1
            start = r + 1 # move over deli    
            slice_len = int(s[i:r])
            end = start + slice_len
            res.append(s[start:end])
            i = end
        return res
             

