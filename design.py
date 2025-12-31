from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        # Maps index to number
        self.index_map = {}
        # Maps number to sorted set of indices
        self.num_indices = {}
        
    def change(self, index: int, number: int) -> None:
        # If index already contains a number, remove it from old number's set
        if index in self.index_map:
            old_num = self.index_map[index]
            self.num_indices[old_num].remove(index)
            # If no more indices for this number, remove the empty set
            if not self.num_indices[old_num]:
                del self.num_indices[old_num]
        
        # Update index_map
        self.index_map[index] = number
        
        # Add index to new number's set
        if number not in self.num_indices:
            self.num_indices[number] = SortedSet()
        self.num_indices[number].add(index)
        
    def find(self, number: int) -> int:
        # Return smallest index for the number if it exists, else -1
        return self.num_indices[number][0] if number in self.num_indices else -1