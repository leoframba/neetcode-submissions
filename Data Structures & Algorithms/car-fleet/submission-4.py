from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with speeds and sort them by position descending
        # (Closest to target comes first)
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = [] # Will store the arrival times of the fleets
        
        for pos, spd in cars:
            # Calculate how long it takes this car to reach the target
            time = (target - pos) / spd
            
            stack.append(time)
            
            # If there are at least two fleets, check for a collision
            # If the car behind (top of stack) arrives in LESS OR EQUAL time 
            # than the fleet ahead of it (second to top), it catches up!
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # It joins the fleet ahead, so we pop its faster time off the stack.
                # It adopts the slower time of the fleet ahead of it.
                stack.pop()
                
        # The number of unique arrival times left in the stack is the number of fleets
        return len(stack)