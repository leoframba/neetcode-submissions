class Solution:

    encode_dict = {
            #"": "/e",
            "/e": "",
            
            " ": "/w",
            "/w": " ",
        }

    def encode(self, strs: List[str]) -> str:
        built_s = "" 
        for i, s in enumerate(strs):

            # empty case
            if not s:
                s = "/e"
            # encode spaces in each string
            strs[i] = strs[i].replace(" ", "/w")
            print(strs[i])
            
            # join
            built_s = built_s + strs[i] + " "

        print(built_s)
        # remove final space
        return built_s
    
    def decode(self, s: str) -> List[str]:
        # empty case
        if not s:
            return []

        d_str = []
        #print(s)
        
        # parse string
        start = 0
        end = 0
        while end < len(s):
            if s[end] == ' ' or end == len(s) - 1:
                cur = s[start:end]
                cur = cur.replace("/w", " ")
                d_str.append(cur)
                start = end + 1
            end += 1
        #print(d_str)
        


        return d_str