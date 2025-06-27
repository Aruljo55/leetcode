class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        
        # If k is 0, we can only take zeros
        if k == 0:
            return zeros
        
        # We can always include all zeros, so start with that count
        max_length = zeros
        
        # Now try to add '1' bits while keeping value <= k
        # We'll use a greedy approach: process from right to left
        # and include '1' bits that contribute least to the value
        
        current_value = 0
        power = 0  # represents 2^power
        ones_count = 0
        
        # Process string from right to left
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                # Check if we can include this '1' bit
                bit_value = 1 << power
                
                if current_value + bit_value <= k:
                    current_value += bit_value
                    ones_count += 1
                    power += 1
                else:
                    # If this bit would make value > k, we can't include any more '1' bits
                    # from this position or to the left
                    break
            # Note: we don't increment power for '0' bits since they don't contribute to value
            # but they do take up positions in our subsequence
        
        return zeros + ones_count


# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1
    s1 = "1001010"
    k1 = 5
    result1 = sol.longestSubsequence(s1, k1)
    print(f"Test 1: s='{s1}', k={k1}")
    print(f"Expected: 5, Got: {result1}")
    
    # Let's trace through this example:
    # s = "1001010", k = 5
    # Processing right to left: 0,1,0,1,0,0,1
    # Include rightmost 0: value = 0
    # Include 1 at power=0: value = 1, ones_count = 1
    # Include 0: value = 1 
    # Include 1 at power=1: value = 1 + 2 = 3, ones_count = 2
    # Include 0: value = 3
    # Include 0: value = 3
    # Include 1 at power=2: value = 3 + 4 = 7 > 5, so stop
    # Total: 4 zeros + 2 ones = 6... still wrong!
    print()
    
    # Test case 2
    s2 = "00101001"
    k2 = 1
    result2 = sol.longestSubsequence(s2, k2)
    print(f"Test 2: s='{s2}', k={k2}")
    print(f"Expected: 6, Got: {result2}")
    print()
    
    # Let me think about this differently...
    # For "1001010" with k=5:
    # We want the longest subsequence that represents a number <= 5
    # 5 in binary is 101
    # Possible subsequences: we need to be more systematic

if __name__ == "__main__":
    test_solution()