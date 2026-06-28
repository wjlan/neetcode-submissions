class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        
        # Create a list of empty lists for frequencies
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Fill the frequency buckets
        for num, count in nums_count.items():
            freq[count].append(num)
        
        # Gather the top k frequent elements
        result = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result  # This line should never be reached with valid inputs


        
            
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in nums_count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

     

        