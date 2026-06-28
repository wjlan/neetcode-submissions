class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        chars = set()
        chars.add(s[0])
        max_len = 1

        i = 0
        for j in range(1, len(s)):
            while s[j] in chars:
                    chars.remove(s[i])
                    i += 1
         
            chars.add(s[j])
            max_len = max(max_len, j - i + 1)
        
        return max_len
        
        