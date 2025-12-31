class Solution:
    def minGroups(self, intervals):
        events = []
        
        # Step 1: Create events for each interval
        for left, right in intervals:
            events.append((left, 1))       # Interval starts
            events.append((right + 1, -1)) # Interval ends
        
        # Step 2: Sort events by time, breaking ties by type (-1 before +1)
        events.sort()

        # Step 3: Sweep line to count active intervals
        max_groups = 0
        current_groups = 0
        
        for _, event_type in events:
            current_groups += event_type  # Update active intervals
            max_groups = max(max_groups, current_groups)
        
        return max_groups
