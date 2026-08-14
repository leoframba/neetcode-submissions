class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        

        # test that we can loop back

        # at any given station we can travel if we have gas
        # check gas

        # choose a start
        # to choose a start we are going to iterate through the entire array start from 0

        n = len(gas)
        for i in range(n):
            dist = 0
            tank = 0
            # attempt to go to the next station -- loop as we keep attempting to go next until we hit our goal
            for j in range(i, i + n):
                
                # logic to wrap
                j = j % n

                # fill gass
                tank += gas[j]

                # verify - can we go to the next station?
                if tank < cost[j]:
                    break # we ran out of gas exit attempt
                else:
                    tank -= cost[j]
                    dist += 1 # if we have enough use it
                # goal check - if we've traveled the len of the list we've done a full loop
                if dist == n:
                    return i
        
        return -1

