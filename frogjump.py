class Solution:
    def canCross(self, stones):
        stone_set = set(stones)
        last_stone = stones[-1]

        # Dictionary: stone_position -> set of jump sizes that can reach here
        jumps = {}
        for s in stones:
            jumps[s] = set()

        # First jump must be 1
        jumps[0].add(0)

        for stone in stones:
            for k in jumps[stone]:
                for step in (k - 1, k, k + 1):
                    if step > 0:
                        next_stone = stone + step
                        if next_stone == last_stone:
                            return True
                        if next_stone in stone_set:
                            jumps[next_stone].add(step)

        return False
