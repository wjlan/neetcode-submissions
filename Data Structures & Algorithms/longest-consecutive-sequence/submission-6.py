class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 not in nums:
                length = 0
                while num in nums:
                    length += 1
                    num += 1
                max_length = max(max_length, length)
        
        return max_length

        