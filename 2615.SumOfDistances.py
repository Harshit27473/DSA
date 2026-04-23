from collections import defaultdict
class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)

        sum_left = defaultdict(int)
        cnt_left = defaultdict(int)

        for i,x in enumerate(nums):
            res[i] += cnt_left[x] * i
            res[i] -= sum_left[x]
            cnt_left[x] += 1
            sum_left[x] += i

        sum_right = defaultdict(int)
        cnt_right = defaultdict(int)

        for i,x in reversed(list(enumerate(nums))):
            res[i] += sum_right[x]
            res[i] -= cnt_right[x] * i

            cnt_right[x] += 1
            sum_right[x] += i
        
        return res