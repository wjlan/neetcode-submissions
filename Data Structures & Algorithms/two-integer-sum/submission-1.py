class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):
            pair = target - num
            if pair in index_map:
                return [index_map[pair], i]
                
            else:
                index_map[num] = i

        return None



        