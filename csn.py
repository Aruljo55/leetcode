class Solution:
    def countSmaller(self, nums):
        count = [0] * len(nums)
        indexed_nums = list(enumerate(nums))  # (index, value)

        def merge_sort(start, end):
            if end - start <= 1:
                return indexed_nums[start:end]
            
            mid = (start + end) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid, end)

            merged = []
            i = j = 0
            while i < len(left) or j < len(right):
                if j == len(right) or (i < len(left) and left[i][1] <= right[j][1]):
                    count[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            return merged
        
        merge_sort(0, len(nums))
        return count
