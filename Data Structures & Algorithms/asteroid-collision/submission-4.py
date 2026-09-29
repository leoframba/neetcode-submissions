class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        right = []
        left = []
        # look for opposite values
        for i in range(len(asteroids)):
            curr = asteroids[i]
            
            # Append it to the right direction stack
            if curr > 0:
                right.append(curr)

            elif curr < 0:
                # check if we have an asteroid coming from the right
               
                # destroy any smaller asteroids
                while right and 0 < right[-1] < abs(curr):
                    right.pop()
                
                # if two asteroids are the same size destroy both
                if right and right[-1] + curr == 0:
                    right.pop()
                    continue

                # if there are no asteroids going right we append
                if not right or right[-1] < 0:
                    right.append(curr) 
                

        return right
                        
                
        
                    
                




        