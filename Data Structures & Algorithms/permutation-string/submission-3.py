class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        for char in s1:
            s1_counts[ord(char) - ord("a")] += 1

        i = 0
        for j in range(len(s2)):
            s2_counts[ord(s2[j]) - ord("a")] += 1
            if j - i + 1 > len(s1):
                s2_counts[ord(s2[i]) - ord("a")] -= 1
                i += 1

            if s1_counts == s2_counts:
                return True
        
        return False
        
            
                

        

        