class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
            
        sequence_counts = {}
        
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            sequence_counts[sequence] = sequence_counts.get(sequence, 0) + 1
        
        return [seq for seq, count in sequence_counts.items() if count > 1]