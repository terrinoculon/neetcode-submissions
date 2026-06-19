class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num,0) + 1
        sorted_freq = (sorted(frequencies, key = frequencies.get, reverse=True))
        return sorted_freq[:k]