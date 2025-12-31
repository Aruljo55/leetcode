class Solution:
    def can_partition_to_sum(self, squared_str, target, index=0, current_sum=0):
        if index == len(squared_str):
            return current_sum == target
        
        for i in range(index + 1, len(squared_str) + 1):
            num = int(squared_str[index:i])
            if self.can_partition_to_sum(squared_str, target, i, current_sum + num):
                return True
        
        return False

    def punishmentNumber(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            squared = i * i
            if self.can_partition_to_sum(str(squared), i):
                total += squared
        return total

# Example Usage:
sol = Solution()
print(sol.punishmentNumber(10))  # Output: 182
print(sol.punishmentNumber(37))  # Output: 1478
