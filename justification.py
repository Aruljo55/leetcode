class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        
        while i < len(words):
            # Pack words into the current line
            line = []
            line_length = 0
            while i < len(words) and line_length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_length += len(words[i])
                i += 1
            
            # Justify the current line
            if i == len(words) or len(line) == 1:  # Last line or single word
                justified_line = " ".join(line)
                justified_line += " " * (maxWidth - len(justified_line))
            else:  # Fully justify
                total_spaces = maxWidth - line_length
                gaps = len(line) - 1
                space_between = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                
                justified_line = ""
                for j in range(gaps):
                    justified_line += line[j] + " " * (space_between + (1 if j < extra_spaces else 0))
                justified_line += line[-1]  # Add the last word
                
            result.append(justified_line)
        
        return result
