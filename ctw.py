class Solution:
    def countDays(self, days, meetings):
        # Step 1: Sort meetings by start time (and end time for tie-breaking)
        meetings.sort()
        
        # Step 2: Merge overlapping intervals
        merged = []
        for meeting in meetings:
            if not merged or merged[-1][1] < meeting[0]:
                merged.append(meeting)
            else:
                merged[-1][1] = max(merged[-1][1], meeting[1])
        
        # Step 3: Calculate the total number of days covered by meetings
        total_meeting_days = 0
        for start, end in merged:
            total_meeting_days += end - start + 1
        
        # Step 4: Subtract the meeting days from the total available days
        available_days = days - total_meeting_days
        return available_days
