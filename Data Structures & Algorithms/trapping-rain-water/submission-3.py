class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        max_area = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[len(height) - 1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for h in range(len(height)):
            max_area += (min(left_max[h], right_max[h]) - height[h])

        return max_area
        
        

            

        