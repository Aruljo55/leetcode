from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        
        # Step 1: Count characters in t
        t_count = Counter(t)
        required = len(t_count)
        
        # Step 2: Sliding window
        left, right = 0, 0
        window_count = defaultdict(int)
        formed = 0
        
        # Step 3: Result variables
        min_length = float("inf")
        result = (0, 0)  # (start, end)
        
        while right < len(s):
            char = s[right]
            window_count[char] += 1
            
            # Check if the current character satisfies the condition
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try to shrink the window
            while left <= right and formed == required:
                char = s[left]
                
                # Update the result if it's the smallest window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = (left, right)
                
                # Remove the character at `left` from the window
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            # Expand the window
            right += 1
        
        # Return the result
        start, end = result
        return s[start:end + 1] if min_length != float("inf") else ""
