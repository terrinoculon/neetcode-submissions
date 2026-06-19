class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies  = {}
        for num in nums:
            frequencies[num] = frequencies.get(num,0) + 1
        buckets = [[] for i in range(len(nums) + 1)]
        for num, count in frequencies.items():
            buckets[count].append(num)
        result = []
        for counts in range(len(buckets) - 1, 0, -1):
            result.extend(buckets[counts])
            if len(result) == k:
                return result