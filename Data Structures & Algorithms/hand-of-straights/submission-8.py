from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # we can differ that n must be a multiple of groupsize
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        counts = Counter(hand)
        sorted_hand = sorted(hand)


        #iter 0 - > n looking for straights
        # when we find an invalid number -> attempt to find a swap

        for i in range(n):
            card = sorted_hand[i]
            # start from the lowest vals as they must be the starts of our seq
            if counts[card] > 0: # if a card is avail we TRY to build a seq
                counts[card] -= 1
                for j in range(1, groupSize):
                    target = card + j
                    # if our target doesn't exist or we've run out the hand is invalid
                    if target not in counts or counts[target] == 0:
                        return False
                    else:
                        counts[target] -= 1 # if we find it we consume one
        
        return True
                


        
        
            
        return True
                

                
                    
                    


            
        