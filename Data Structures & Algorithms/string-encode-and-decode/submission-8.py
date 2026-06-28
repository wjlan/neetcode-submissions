class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            str_len = len(s)
            encoded_string += (str(str_len) + "#" + s)
        
        return encoded_string



    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            str_len = int(s[i : j])
            decoded_string.append(s[j + 1 : j + 1 + str_len])
            i = j + 1 + str_len

        return decoded_string




