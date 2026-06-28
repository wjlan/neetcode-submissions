from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            s_key = "".join(sorted(s))
            groups[s_key].append(s)

        return list(groups.values())


        