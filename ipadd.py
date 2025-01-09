class Solution:
    def restoreIpAddresses(self, s):
        def is_valid(segment):
            # Check if the segment is valid: 0 <= int(segment) <= 255 and no leading zeros
            return 0 <= int(segment) <= 255 and (segment == "0" or not segment.startswith("0"))
        
        def backtrack(start, path):
            # If we have 4 segments and are at the end of the string, add to result
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return
            
            # Try all possible splits for the next segment
            for length in range(1, 4):  # Segment lengths are 1 to 3
                if start + length <= len(s):
                    segment = s[start:start+length]
                    if is_valid(segment):
                        backtrack(start + length, path + [segment])
        
        result = []
        backtrack(0, [])
        return result
