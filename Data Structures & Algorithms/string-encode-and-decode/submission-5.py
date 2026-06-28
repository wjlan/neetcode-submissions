class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += (str(len(s)) + "#" + s)
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
        
            length = int(s[i : j])
            word = s[j + 1 : j + length + 1]
            decoded_str.append(word)
            
            i = j + length + 1 
        
        return decoded_str
                


