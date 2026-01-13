class Solution:
    def originalDigits(self, s):
        from collections import Counter

        count = Counter(s)
        res = [0] * 10

        res[0] = count['z']
        res[2] = count['w']
        res[4] = count['u']
        res[6] = count['x']
        res[8] = count['g']

        res[1] = count['o'] - res[0] - res[2] - res[4]
        res[3] = count['h'] - res[8]
        res[5] = count['f'] - res[4]
        res[7] = count['s'] - res[6]
        res[9] = count['i'] - res[5] - res[6] - res[8]

        output = []
        for i in range(10):
            output.append(str(i) * res[i])

        return ''.join(output)
