class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        answer = [0] * n

        # Left to right pass
        count = 0  # Number of balls to the left
        moves = 0  # Accumulated moves
        for i in range(n):
            answer[i] += moves
            count += int(boxes[i])
            moves += count

        # Right to left pass
        count = 0  # Number of balls to the right
        moves = 0  # Accumulated moves
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            count += int(boxes[i])
            moves += count

        return answer
