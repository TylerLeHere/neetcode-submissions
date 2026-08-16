class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #It takes ceil(x/k) time to finish the x pile when Koko eats at a rate of k. However, we must also ensure at this rate, k, Koko can finish eating all the piles within h hours, Upper Bound for K is the maximum size of all the piles. We can use the binary search with the upper bound of k is max(piles)
        
        #Scan the k value from 1 to its max
        lowerBound = 1
        upperBound = max(piles)
        result = lowerBound
        while lowerBound <= upperBound:
            #Calculate the middle index
            middleIndex = (lowerBound + upperBound) // 2
            totalTime = 0
            for pile in piles:
                totalTime = totalTime + math.ceil(pile / middleIndex)
            
            if totalTime <= h:
                result = middleIndex
                upperBound = middleIndex - 1
            else:
                lowerBound = middleIndex + 1
        
        return result




