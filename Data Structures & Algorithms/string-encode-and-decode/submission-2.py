class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(item)}.{item}" for item in strs])

    def decode(self, s: str) -> List[str]:
        current_head = 0
        outputs = []
        while (current_head<len(s)):
            next_split = s.find(".", current_head)            
            cur_length = int(s[current_head:next_split])            
            outputs.append(s[next_split+1:cur_length+next_split+1])
            current_head = (next_split + cur_length + 1)
        return outputs