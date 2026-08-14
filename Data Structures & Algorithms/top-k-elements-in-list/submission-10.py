class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        print(map)
        ans = []
        while k > 0: 
            max = None
            for key in map:
                if max == None:
                    print("hit")
                    max = key 
                if map[key] > map[max]:
                    print(map[key])
                    print(map[max])

                    max = key
                    
                print(f"max {max}")
            
            del map[max]
            
            ans.append(max)
            
            k -= 1   
        
        return ans

        