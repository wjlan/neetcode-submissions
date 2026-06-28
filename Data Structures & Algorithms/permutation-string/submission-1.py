class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1)
        while right <= len(s2):
            if self.isPermutation(s1, s2[left: right]):
                return True
            else:
                left += 1
                right += 1
        return False
         
    def isPermutation(self, s1, s2):
        if len(s1) != len(s2):
            return False
        freq = [0] * 26
        for char in s1:
            freq[ord(char) - ord('a')] += 1
        for char in s2:
            freq[ord(char) - ord('a')] -= 1
        for v in freq:
            if v != 0:
                return False
        return True
        