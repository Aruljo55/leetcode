class Solution:
    def minOperations(self, grid, x):
        # Flatten the grid
        flat_grid = [num for row in grid for num in row]
        
        # Check if all differences are divisible by x
        first_value = flat_grid[0]
        for value in flat_grid:
            if abs(value - first_value) % x != 0:
                return -1
        
        # Sort the grid and find the median
        flat_grid.sort()
        median = flat_grid[len(flat_grid) // 2]
        
        # Calculate the total number of operations to convert all values to the median
        operations = 0
        for value in flat_grid:
            operations += abs(value - median) // x
        
        return operations
