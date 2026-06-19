class Solution:    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for word in strs:
            signature = "".join(sorted(word))
            if signature in output:
                output[signature].append(word)
            else:
                output[signature] = [word]
        return list(output.values())
