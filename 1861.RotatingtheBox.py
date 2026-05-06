class Solution(object):
    def rotateTheBox(self, box):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        rows, cols = len(box), len(box[0])

        for r in range(rows):
            i = cols - 1
            for c in reversed(range(cols)):
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == "*":
                    i = c-1

        res = []

        for c in range(cols):
            col =[]
            for r in reversed(range(rows)):
                col.append(box[r][c])
            
            res.append(col)
        return res