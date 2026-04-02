class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_mapping: dict[int, int] = defaultdict(lambda: 0)
        for num in nums:
            frequency_mapping[num] += 1

        return [key for key, val in sorted(frequency_mapping.items(), key=lambda x: x[1], reverse=True)][:k]