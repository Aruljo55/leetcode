class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        visited_A = set()
        visited_B = set()
        prefix_common = []
        
        for i in range(n):
            visited_A.add(A[i])
            visited_B.add(B[i])
            
            # Count the intersection of visited elements
            common_count = len(visited_A & visited_B)
            prefix_common.append(common_count)
        
        return prefix_common
