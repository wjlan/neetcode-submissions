class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        for num, c in count.items():
            freq[c].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if len(res) < k:
                    res.append(n)

        return res
                



        