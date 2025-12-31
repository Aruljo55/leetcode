class Solution:
    def partitionLabels(self, s: str):
        # Step 1: Record the last occurrence of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        partitions = []
        start = 0
        end = 0
        
        # Step 2: Iterate through the string and partition the string
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])  # Update the end of the current partition
            
            # If we reach the end of the current partition, finalize the partition
            if i == end:
                partitions.append(i - start + 1)  # Add the size of the current partition
                start = i + 1  # Start a new partition
        
        return partitions
