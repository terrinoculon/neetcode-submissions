class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nR = len(matrix)
        nC = len(matrix[0])
        t=0
        b = nR-1
        row = -1
        while t<=b:
            mid = t + (b-t)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                row = mid
                break
            elif matrix[mid][0]> target:
                b = mid - 1
            elif matrix[mid][-1]<target:
                t = mid +1
        if row == -1:
            return False
        l = 0
        r = nC-1
        while l<=r:
            mid = l + (r-l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return False