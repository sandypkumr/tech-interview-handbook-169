from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])
            if left < right and top < bottom:
                for j in range(right - 1, left, -1):
                    res.append(matrix[bottom][j])
                for i in range(bottom, top, -1):
                    res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res
