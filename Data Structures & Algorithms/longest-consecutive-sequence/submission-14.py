class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums_set = set(nums)

        for num in nums_set:
            count = 1
            while (num + 1) in nums_set:
                count += 1
                num += 1
            max_length = max(max_length, count)

        return max_length

                

        
            

        