from collections import defaultdict

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # use the first str to compare
        first_s = strs[0]
        for i in range(len(first_s)):
            for s in strs:
                if i == len(s) or s[i] != first_s[i]:
                    return strs[0][:i]
        
        return strs[0]
           
        