class Solution(object):
    def minOperations(self, grid, x):
        m, n = len(grid), len(grid[0])
        total = m * n
        left = grid[0][0] % x

        mini, maxi = grid[0][0], grid[0][0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != left:
                    return -1
                mini = min(mini, grid[i][j])
                maxi = max(maxi, grid[i][j])

        k, low, high, median = total // 2, mini, maxi, mini
        while low <= high:
            mid = low + (high - low) // 2
            count = sum(1 for i in range(m) for j in range(n) if grid[i][j] <= mid)
            if count <= k:
                low = mid + 1
            else:
                median = mid
                high = mid - 1

        totalOperations = 0
        for i in range(m):
            for j in range(n):
                totalOperations += abs(grid[i][j] - median) // x

        return totalOperations