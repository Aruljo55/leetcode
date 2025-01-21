from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        neighbors = defaultdict(list)
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)

        queue = deque([[beginWord]])
        visited = set([beginWord])
        results = []
        found = False

        while queue and not found:
            level_visited = set()
            for _ in range(len(queue)):
                path = queue.popleft()
                current_word = path[-1]
                for i in range(len(current_word)):
                    pattern = current_word[:i] + "*" + current_word[i+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor == endWord:
                            found = True
                            results.append(path + [neighbor])
                        elif neighbor not in visited:
                            queue.append(path + [neighbor])
                            level_visited.add(neighbor)
            visited.update(level_visited)

        return results
