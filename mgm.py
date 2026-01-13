from collections import deque

class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        queue = deque()
        queue.append((startGene, 0))
        visited = set([startGene])
        genes = ['A', 'C', 'G', 'T']

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps

            for i in range(8):
                for g in genes:
                    if g != gene[i]:
                        mutated = gene[:i] + g + gene[i+1:]
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, steps + 1))

        return -1
