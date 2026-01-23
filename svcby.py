from collections import Counter

class Solution:
    def frequencySort(self, s):
        freq = Counter(s)

        result = []
        for ch, count in sorted(freq.items(), key=lambda x: -x[1]):
            result.append(ch * count)

        return "".join(result)
