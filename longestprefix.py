class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Start by assuming the first word is the common prefix
        prefix = strs[0]
        
        # Compare this prefix with each string in the array
        for string in strs[1:]:
            # Reduce the prefix size until it matches the beginning of the string
            while string[:len(prefix)] != prefix and prefix:
                # Remove the last character from the prefix
                prefix = prefix[:-1]
            
            # If at any point the prefix becomes an empty string, return ""
            if not prefix:
                return ""
        
        return prefix
