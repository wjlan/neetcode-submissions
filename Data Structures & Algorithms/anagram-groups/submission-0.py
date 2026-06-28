class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(list(s)))
            anagrams[sorted_s].append(s)
       
        
        return list(anagrams.values())

        