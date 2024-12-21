class Solution:
    def generateParenthesis(self, n):
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: if the current string is well-formed and has the max length
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # If we can add an opening parenthesis, do so
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
            
            # If we can add a closing parenthesis, do so
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
        
        # Start the backtracking process
        backtrack("", 0, 0)
        return result

