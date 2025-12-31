class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def findWords(self, board, words):
        def backtrack(node, row, col, path):
            char = board[row][col]
            if char not in node.children:
                return

            node = node.children[char]
            path += char

            if node.is_word:
                result.add(path)

            temp, board[row][col] = board[row][col], "#"

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] != "#":
                    backtrack(node, nr, nc, path)

            board[row][col] = temp

        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True

        result = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                backtrack(root, row, col, "")

        return list(result)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(solution.findWords(board, words))  # Output: ['eat', 'oath']

    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    print(solution.findWords(board, words))  # Output: []