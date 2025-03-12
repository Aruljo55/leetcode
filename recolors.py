class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Initialize the count of white blocks in the first window of size k
        min_ops = blocks[:k].count('W')
        curr_ops = min_ops

        # Slide the window across the string
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':  # Remove the leftmost block from the window
                curr_ops -= 1
            if blocks[i] == 'W':  # Add the new rightmost block to the window
                curr_ops += 1
            
            min_ops = min(min_ops, curr_ops)  # Track the minimum operations

        return min_ops
