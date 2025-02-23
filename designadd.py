class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word

            char = word[i]
            if char == '.':
                return any(dfs(child, i + 1) for child in node.children.values())

            if char in node.children:
                return dfs(node.children[char], i + 1)

            return False

        return dfs(self.root, 0)

# Example usage
if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))  # Output: False
    print(wordDictionary.search("bad"))  # Output: True
    print(wordDictionary.search(".ad"))  # Output: True
    print(wordDictionary.search("b.."))  # Output: True