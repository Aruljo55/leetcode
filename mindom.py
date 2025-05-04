class Solution:
    def minDominoRotations(self, tops, bottoms):
        def check(x):
            rotations_a = rotations_b = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotations_a += 1
                elif bottoms[i] != x:
                    rotations_b += 1
            return min(rotations_a, rotations_b)
        
        result = check(tops[0])
        if result != -1 or tops[0] == bottoms[0]:
            return result
        return check(bottoms[0])
