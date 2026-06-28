class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] = res[j] * right
            right = right * nums[j]

        return res

        
        
        