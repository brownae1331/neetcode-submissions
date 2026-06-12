class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            encode_str = encode_str + str(len(s)) + "#" + s
        return encode_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num_str = ""
            input_str = ""
            while s[i] != "#":
                num_str = num_str + s[i]
                i += 1
            start = i + 1
            end = i + 1 + int(num_str)
            i = end
            for ii in range(start, end):
                input_str = input_str + s[ii]
            res.append(input_str)
        return res
