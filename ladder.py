from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        neighbors = defaultdict(list)
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            current_word, steps = queue.popleft()
            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i+1:]
                for neighbor in neighbors[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
        return 0
