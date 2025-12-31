from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        # Helper function to check if the string is valid
        def is_valid(string):
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0
        
        # BFS initialization
        result = []
        visited = set()
        queue = deque([s])
        visited.add(s)
        found_valid = False
        
        while queue:
            current_string = queue.popleft()
            
            # If it's valid, add to result, and mark as found_valid
            if is_valid(current_string):
                result.append(current_string)
                found_valid = True
            
            # If we've already found a valid string, we don't need to continue with more removals
            if found_valid:
                continue
            
            # Try removing one parenthesis at a time
            for i in range(len(current_string)):
                if current_string[i] not in ['(', ')']:
                    continue
                next_string = current_string[:i] + current_string[i+1:]
                if next_string not in visited:
                    visited.add(next_string)
                    queue.append(next_string)
        
        return result
