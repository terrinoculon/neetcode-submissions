class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(item)) + "#" + item for item in strs])

    def decode(self, s: str) -> List[str]:
        current_head = 0
        outputs = []

        while (current_head<len(s)):
            delimiter_pos = s.find("#", current_head)
            cur_length = int(s[current_head:delimiter_pos])            
            outputs.append(s[delimiter_pos+1:cur_length+delimiter_pos+1])
            current_head = delimiter_pos + 1 + cur_length
        return outputs