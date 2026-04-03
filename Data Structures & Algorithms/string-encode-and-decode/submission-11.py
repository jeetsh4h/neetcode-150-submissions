class Solution:
    LENGTH_DELIM = ","
    BLOCK_DELIM = "|"
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        lengths = []
        content = ""
        for word in strs:
            lengths.append(len(word))
            content += word

        lengths = list(map(str, lengths))
        return f"{self.LENGTH_DELIM.join(lengths)}{self.BLOCK_DELIM}{content}"

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        lengths, content = s.split(self.BLOCK_DELIM, 1)
        lengths = list(map(int, lengths.split(self.LENGTH_DELIM)))
        decoded = []
        total = 0
        for length in lengths:
            decoded.append(content[total:total+length])
            total += length

        return decoded