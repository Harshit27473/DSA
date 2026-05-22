class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)

        # Find rotation index (minimum element index)
        lo, hi = 0, n - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        rot = lo

        # Normal binary search using rotated indices
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real

            if nums[real] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1