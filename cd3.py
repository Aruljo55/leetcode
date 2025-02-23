class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        bucket = {}
        width = valueDiff + 1

        for i, num in enumerate(nums):
            bucket_id = num // width

            if bucket_id in bucket:
                return True

            if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) <= valueDiff:
                return True

            if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) <= valueDiff:
                return True

            bucket[bucket_id] = num

            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // width]

        return False