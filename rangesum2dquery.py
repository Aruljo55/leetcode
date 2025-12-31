class NumMatrix:

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return

        # Initialize the prefix sum matrix
        m, n = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the prefix sum matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix_sum[i][j] = (
                    matrix[i - 1][j - 1] +
                    self.prefix_sum[i - 1][j] +
                    self.prefix_sum[i][j - 1] -
                    self.prefix_sum[i - 1][j - 1]
                )

    def sumRegion(self, row1, col1, row2, col2):
        # Adjust the 1-based indexing of the prefix_sum
        return (
            self.prefix_sum[row2 + 1][col2 + 1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row1][col1]
        )
