class Solution:
    def palindromePairs(self, words):
        def is_palindrome(check):
            return check == check[::-1]

        word_lookup = {word[::-1]: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]

                # Case 1: prefix is palindrome, check if reversed suffix exists
                if is_palindrome(prefix):
                    back = word_lookup.get(suffix)
                    if back is not None and back != i:
                        result.append([back, i])

                # Case 2: suffix is palindrome, check if reversed prefix exists
                # j != len(word) avoids duplicates
                if j != len(word) and is_palindrome(suffix):
                    front = word_lookup.get(prefix)
                    if front is not None and front != i:
                        result.append([i, front])

        return result
