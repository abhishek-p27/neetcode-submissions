class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r 

        while l <= r: 
            k = (l + r) // 2
            Time = 0 
            for p in piles: 
                Time += math.ceil(float(p)/ k)
                if Time > h: 
                    break
            if Time <= h: 
                result = k
                r = k - 1 
            else: 
                l = k + 1 
        return result 