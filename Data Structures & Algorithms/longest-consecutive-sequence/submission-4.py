class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
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
        # nums = set(nums)
        # max_length = 0
        # visited = set()
        # for num in nums:
        #     if num - 1 not in nums:
        #         length = 0
        #     if num not in visited:
        #         while num in nums:
        #             visited.add(num)
        #             length += 1
        #             num += 1
        #         max_length = max(max_length, length)
        
        # return max_length

        