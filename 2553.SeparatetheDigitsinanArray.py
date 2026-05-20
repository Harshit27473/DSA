class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for num in nums:

            s = str(num)

            for ch in s:

                result.append(int(ch))

        return result
    