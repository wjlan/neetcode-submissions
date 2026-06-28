class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        max_len = 1
        char_set = set()
        char_set.add(s[i])
        for j in range(1, len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            max_len = max(max_len, j - i + 1)
            char_set.add(s[j])
    
        return max_len
                


        