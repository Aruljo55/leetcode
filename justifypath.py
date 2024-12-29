class Solution:
    def simplifyPath(self, path):
        stack = []
        
        # Split the path by slashes
        components = path.split("/")
        
        for component in components:
            if component == "" or component == ".":
                continue  # Skip empty or current directory references
            elif component == "..":
                if stack:  # Go up one level if possible
                    stack.pop()
            else:
                stack.append(component)  # Valid directory or file
        
        # Join stack to construct the canonical path
        return "/" + "/".join(stack)
