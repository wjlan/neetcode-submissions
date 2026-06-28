class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in mapping:
                return [mapping[pair], i]
            mapping[num] = i
        
        return -1


        


        