class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = {}
        for s in strs:
            s_key = "".join(sorted(s))
            if s_key in groups:
                groups[s_key].append(s)
            else:
                groups[s_key] = [s]
        
        for v in groups.values():
            res.append(v)

        
        return res


        