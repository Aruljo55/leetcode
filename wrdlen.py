class Solution:
    def maxProduct(self, words):
        n = len(words)
        masks = [0] * n
        lengths = [len(word) for word in words]

        # Create bitmasks for each word
        for i in range(n):
            mask = 0
            for char in words[i]:
                mask |= 1 << (ord(char) - ord('a'))
            masks[i] = mask

        max_product = 0

        # Compare pairs of words
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:  # no common letters
                    max_product = max(max_product, lengths[i] * lengths[j])

        return max_product
