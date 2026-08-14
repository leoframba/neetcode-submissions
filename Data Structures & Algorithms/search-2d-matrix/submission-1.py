class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ##find the row
        f = 0
        r = len(matrix) - 1

        target_list = -1

        while f <= r:
            m = ((r - f) // 2) + f
            bounds = (matrix[m][0], matrix[m][-1])

            if target < bounds[0]:
                r = m - 1
            
            if target > bounds[1]:
                f = m + 1
            
            if target >= bounds[0] and target <= bounds[1]:
                target_list = m
                print("hit")
                break
        
        if target_list == -1:
            return False
        
        f = 0
        r = len(matrix[target_list]) - 1

        while f <= r:
            m = ((r - f) // 2) + f
            cur = matrix[target_list][m]

            if target > cur:
                f = m + 1
            
            if target < cur:
                r = m - 1
            
            if target == cur:
                return True

        return False


        

        