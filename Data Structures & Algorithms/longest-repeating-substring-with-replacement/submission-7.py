class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = [0] * 26
        max_len = 1
        i = 0
        for j in range(len(s)):
            char_counts[ord(s[j]) - ord("A")] += 1
            while (j - i + 1) - max(char_counts) > k:   
                char_counts[ord(s[i]) - ord("A")] -= 1
                i += 1
                
            max_len = max(max_len, j - i + 1)

        return max_len



        
            
            

            



        