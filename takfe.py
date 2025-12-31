from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Create a list of empty buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)

        result = []
        # Traverse buckets from highest frequency to lowest
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result
