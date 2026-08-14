class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        tup_list = list(zip(position, speed))
        sorted_list = sorted(tup_list)
        

        
        time = []
        for i in range(len(sorted_list) - 1, -1, -1):
            cur = sorted_list[i]
            time_to_target = (target - cur[0]) / cur[1]
            time.append(time_to_target)

        res = 0
        cur = 0
        for i in time:
            if i > cur:
                res += 1
                cur = i
        
        return res


            
            


            
            
            

            

        
        