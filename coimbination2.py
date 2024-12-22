class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort the candidates to handle duplicates
        result = []
        
        # Backtracking function
        def backtrack(start, current_combination, remaining_target):
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > remaining_target:
                    break  # Stop further exploration if the candidate exceeds the target
                
                # Include the candidate and continue exploring
                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, remaining_target - candidates[i])
                current_combination.pop()  # Backtrack
        
        backtrack(0, [], target)
        return result
