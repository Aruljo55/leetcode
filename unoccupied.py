import heapq

class Solution:
    def smallestChair(self, times, targetFriend):
        # Step 1: Sort friends by arrival time
        times = sorted(enumerate(times), key=lambda x: x[1][0])  # [(index, [arrival, leaving])]
        
        available_chairs = []  # Min-heap for available chair numbers
        occupied_chairs = []   # Min-heap for (leaving_time, chair_number)
        chair_map = {}         # Maps friend index to their assigned chair
        
        chair_id = 0  # Next available chair number

        # Step 2: Process each friend in order of arrival
        for friend_id, (arrival, leaving) in times:
            # Free up chairs that are now available
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                _, freed_chair = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, freed_chair)
            
            # Assign the smallest available chair
            if available_chairs:
                assigned_chair = heapq.heappop(available_chairs)
            else:
                assigned_chair = chair_id
                chair_id += 1  # Move to the next chair if none are available

            # Track assigned chair
            chair_map[friend_id] = assigned_chair
            heapq.heappush(occupied_chairs, (leaving, assigned_chair))

            # Return the chair assigned to targetFriend
            if friend_id == targetFriend:
                return assigned_chair
