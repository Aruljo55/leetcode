class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        lengths = [1]  # Initial length of word = "a"

        # Step 1: compute the lengths after each operation
        for op in operations:
            lengths.append(lengths[-1] * 2)

        char = 'a'  # initial character

        # Step 2: go backward through operations
        for i in range(len(operations) - 1, -1, -1):
            op = operations[i]
            prev_len = lengths[i]

            if k > prev_len:
                k -= prev_len
                if op == 1:
                    # increment char by 1 in the alphabet (cyclic)
                    char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))

        return char
