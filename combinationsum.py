class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        # Backtracking function to find all combinations
        def backtrack(start, current_combination, remaining_target):
            # If the remaining target is zero, add the current combination to the result
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            
            # Iterate through the candidates starting from `start` to avoid duplicates
            for i in range(start, len(candidates)):
                if candidates[i] > remaining_target:
                    continue  # Skip candidates that exceed the remaining target
                
                # Include the candidate and continue exploring
                current_combination.append(candidates[i])
                backtrack(i, current_combination, remaining_target - candidates[i])
                # Backtrack by removing the last added element
                current_combination.pop()
        
        # Start backtracking
        backtrack(0, [], target)
        return result
