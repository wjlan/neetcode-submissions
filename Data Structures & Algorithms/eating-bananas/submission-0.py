class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if self.can_eat(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left
    
    def can_eat(self, piles, k, h):
        result = 0  
        for pile in piles:
            if pile % k == 0:
                result += (pile // k)
            else:
                result += (pile // k + 1)
         
        return result <= h
            

        