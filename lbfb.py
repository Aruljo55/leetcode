class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len = {0: 0}

        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')
            if '.' in name:
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1  # Add 1 for '/'
        
        return max_len
