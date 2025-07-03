class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1  # The word itself is always valid

        i = 0
        while i < len(word):
            j = i
            while j + 1 < len(word) and word[j + 1] == word[i]:
                j += 1
            group_length = j - i + 1

            if group_length >= 2:
                count += group_length - 1  # Each group can remove 1 character in multiple ways

            i = j + 1  # Move to the next group

        return count
