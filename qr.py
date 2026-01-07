class Solution:
    def reconstructQueue(self, people):
        # Sort by height descending, and k ascending
        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []

        # Insert each person at index k
        for p in people:
            queue.insert(p[1], p)

        return queue
