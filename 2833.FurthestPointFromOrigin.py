class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        left = 0
        right = 0
        dash = 0

        for ch in moves:
            if ch == 'L':
                left += 1
            elif ch == 'R':
                right += 1
            else:
                dash += 1

        return abs(left-right ) + dash