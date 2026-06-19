class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num,0) + 1
        print(frequencies)
        sorted_freq = dict(sorted(frequencies.items(), key = lambda item:item[1], reverse=True))
        return list(sorted_freq.keys())[:k]